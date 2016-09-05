import re, json, string
from collections import OrderedDict, defaultdict


class GrammarStructure:
    g_reg = r'^(?P<lhs>[A-Z]+)\s+->(?P<rhs>.*)$'
    G = {}

# 作用：从文件中将记录的映射读取成字典
    def __init__(self, g_file='static/sample_grammarstructure.cfg'):
        for l in open(g_file):
            l = l.strip()
            m = re.match(self.g_reg, l)
            rhs = ['xx' if re.match(r'None', y)#
                   else y.strip().strip("'")#
                   for y in  m.group('rhs').split('|')]
            try:
                self.G[m.group('lhs')].extend(rhs)
            except KeyError:
                self.G[m.group('lhs')] = rhs

# 作用：从文件中的有尖括号的那部分读取出来，作为字典映射
    def getTermFiles(self):
        fl_list = {}
        for k, v in self.G.items():
            reg = re.compile(r'\<(?P<name>.+)\>')
            for r in v:
                m = reg.match(r)
                if m:#
                    fl_list[k] = m.group('name')
        return fl_list

    def to_json(self):
        return json.dumps(self.G)

    def __str__(self):
        return '\n'.join(['%s -> %s' % \
                              (lhs, ' | '.join(rhs))#
                          for lhs, rhs in self.G.items()])

class Token:
    def __init__(self, val=None, type_=0, meta=None):
        self.value = val    # string/Token
        self.type_ = type_  # 0(NonT), 1(Terminal), 2(others)
        self.meta  = meta   # Mangles

    def __str__(self):
        return str([self.value, self.type_])

    def show(self):
        return self.value

    def getval(self):
        return self.value

    def __init__(self, strng):
        m = re.match(r"'(.*)'", strng)
        if m:
            self.value = m.group(1)
            self.type_ = 1   # Terminal
            self.meta = ''
        else:
            self.value = strng
            self.type_ = 0
            self.meta  = strng

    def __eq__(self, other):
        return self.value == other.value and self.type_ == other.type_


class Rule:
    def __init__(self, rhs, freq=0):
        if isinstance(rhs, list):
            self.rhs = rhs    # list of Tokens
        else:
            self.rhs = [Token(x) for x in rhs.split()]
        self.freq= freq

    def __eq__(self, other):
        if len(self.rhs) != len(other.rhs):
            return False
        for x, y in zip(self.rhs, other.rhs):
            if x != y: return False
        return True

# 个人理解：这里的规则存放有点像树，tree = (l,r),
# 而 r 可能会等于 r = (r_l,r_r)...有点像那个。。。。树转换成的二叉树，
# 然后最低端的元素（l,r）直接就是两个字符串
"""
使用说明：
初始化的时候可以将规则存入。                           (l, r)
l：左规则，为string                                       / \
r：右规则，可以为ParseTree                           (l, r) (l, r)
tree:存储规则，里面放的是tuple（l，r）
当确认使用NonT之后，要将这个节点存入这棵树里面，确定这个NonT节点和其他规则之间的关系
"""
class ParseTree(object):
    def __init__(self, l=None, r=None):

        # tree中存放了（左规则→右规则），l为string，r为tree（另一个list）
        self.tree = []
        if l and r:
            self.add_rule((l,r))

    def add_rule(self, rule, f=0):
        self.tree.append(rule)

    def extend_rules(self, ptree):
        self.tree.extend(ptree.tree)


        # 此功能为拿出这颗树的最顶端节点（最左边），然后把其 r 中的所有 l 视为其子节点，
        # 并把 r 中所有的 l 的左节点（rl1，rl2 等等）中的 l 中内容去掉
        # 最终返回一个 tuple（l，r），此时的r是一个左节点子节点的集合


    def get_rule(self):
        # 拿出第一个规则
        rule = self.tree[0]
        # 拿出第一个规则的l
        lhs = rule[0]
        # 把规则转换为Lxx_的形式，然后方便查在RuleSet中查找右规则
        rep_str = '%s_' % lhs
        # 存放右规则，其中吧Lxx_形式的规则全部替换成''，注意这里的rule【1】为右规则，右规则里面可能放了很多的（l,r），这里吧右规则的l去拿出来
        rhs = ''.join([ k[0].replace(rep_str, '')  #
                      for k in rule[1]])
        return lhs, rhs

# 此函数返回有一个RuleSet类（用字典存储有哪些规则G[l][r] = 出现频率）,这里通过调用函数，设置每个节点对应的规则和其概率

    def rule_set(self):
        r = RuleSet()

        # 拿出所有的左规则（L_%s)
        for p in self.tree:

            # 假如右规则直接就是字（到达节点）
            if isinstance(p[1], basestring):
                r.add_rule(p[0], p[1])
            else:
                r.add_rule(*(self.get_rule()))
                r.update_set(p[1].rule_set())
        return r

    def __str__(self):
        return str(self.tree)

    def __repr__(self):
        return str(self.tree)

    def __nonzero__(self):
        return bool(self.tree)

    def __getitem__(self, index):
        return self.tree[index]

    def __len__(self):
        return len(self.tree)

    def save(self, fname):
        json.dumps(self.tree, fname)


"""
基础类，用于设置规则，G为一个二重字典（？）G[l][r]中存储了规则(l->r)发生的规则。

G：也就是这个字典

"""
class RuleSet(object):
    """
    Set of rules, l -> r1 | r2 | r3
    """
    def __init__(self, l=None, r=None, d=None):

        # G是一个字典包字典，l为非结尾规则，r为结尾规则
        # d为某规则字典（也是字典包字典），字典的键为规则，值为出现次数
        self.G = defaultdict(OrderedDict)
        if l and r:
            self.add_rule(l,r)
        if d:
        # k是l规则，v是r规则和其对应的（字典）
            for k,v in d.items():
                self.G[k].update(v)

# 该方法的意思是：存下当前方法（存在字典G中，G[l][r]表示l->r规则的出现概率），f为出现频率
    def add_rule(self, l, r, f=0, rule=None):
        if rule:
            l = rule[0]
            r = rule[1]
        self.G[l][r] = self.G[l].get(r, 1)+f
# 该方法是用已知的gui#
    def update_set(self, T, with_freq=False, freq=0):

        # 这里的l是左边的规则，v是r规则和频率
        for l,v in T.items():

            if with_freq:
                # 这里的f是r规则对应的频率
                for r,f in v.items():
                    f = freq if freq > 0 else f
                    self.G[l][r] = self.G[l].get(r,0)+f
            else:
                self.G[l].update(v)

    def __getitem__(self, k):
        return self.G.__getitem__(k)

    def __iter__(self):
        return iter(self.G)

    def __keytransform__(self, key):
        return key


    def save(self, outf):
        # sanity check（语法检测）ascii——lowercase是所有的小写字母
        for c in string.ascii_lowercase:
            k = 'L_%s' % c

        # 这里是给每个L_a,L_b...等等设置一个频率，其中a或者A都是其中的R规则的频率
            self.G[k] = self.G.get(k, {c:1, c.upper(): 1})
        json.dump(self.G, outf, sort_keys=True,
                  separators=(',', ':'), indent=2)

    def load(self, in_file):
        self.G = json.load(open_(in_file),
                           object_pairs_hook=OrderedDict)

    def __str__(self):
        return json.dumps(self.G, separators=(',',':'),
                   sort_keys=True, indent=2)

    def items(self):
        return self.G.items()

    def __nonzero__(self):
        return bool(self.G)


class Tweaker:
    rules = {'3': 'e',
             '4': 'a',
             '@': 'a',
             '$': 's',
             '0': 'o',
             '1': 'i',
             'z': 's'
             }

    def getTweakerRules(self, mangle_fl=None ):
        try:
            rules = {}
            for l in open(mangle_fl):
                l = l.strip().split(':')
                rules[l[0]] = l[1]
        except IOError:
            print (mangle_fl+'-- could not be opend! Tweaker set is empty.')
        return rules;

    def __init__(self, mangle_fl=None):
        if mangle_fl:
            self.rules = self.getTweakerRules(mangle_fl)

    def tweak ( self, s ):
        if len(s)==1:#
            try: return self.rules[s]
            except KeyError: return s;
        else:
            return ''.join([self.tweak(c) for c in s])


# 专门处理键盘键位的类
class KeyBoard:
    offset = 50; # to handle negetive!!!!
    layout_matrix = [
        "1234567890-=",
        "!@# $%^&*()_+",
        "qwertyuiop[]|",
        "QWERTYUIOP{}\\",
        "asdfghjkl;'",
        'ASDFGHJKL:"',
        "zxcvbnm,./",
        "ZXCVBNM<>?"
        ]#
    def __init__(self, keyboard_layout_fl=None):
        self.layout_map = {}
        for i, row in enumerate(self.layout_matrix):
            for j,c in enumerate(row):
                self.layout_map[c] = (i/2,j)

    def isShift(self, c):
        p=self.layout_map[c];
        return int(self.layout_matrix[2*p[0]][p[1]] != c)

    def dist(self,p1, p2):
        dy = p2[0]-p1[0] + self.offset
        dx = p2[1]-p1[1] + self.offset
        return (dy,dx)

    def encode_keyseq( self, seq ):
        if not seq[1]: seq[1] = (0,0)
        a = (seq[1][0]<<24)|(seq[1][1]<<16)|(seq[2]<<8)|seq[3]
        return a

    def decode_keyseq( self, a ):
        return [((0xff000000&a) >> 24, (0xff0000&a) >> 16),
                (0xff00&a) >> 8, 0xff&a]

    def generate_passqord_fromseq( self, seq ):
        p = ''
        for s in seq:
            p += s[0]
            pos = list(self.layout_map[s[0]])
            n = self.decode_keyseq(s[1])
            for i in range(n[2]):
                pos[0] += (n[0][0] - self.offset)
                pos[1] += (n[0][1] - self.offset)
                p += self.layout_matrix[pos[0]*2 + n[1]][pos[1]]
        return p

    def IsKeyboardSeq(self, w):
        if len(w)<5 : return 99.0, []
        M = self.layout_map
        score = 0;
        try:
            pos = [M[c] for c in w]
        except KeyError:
            return 99.0, []
        dist_pos = [self.dist(pos[i-1], pos[i])#
                    for i in range(1,len(w))]
        group_dist_pos = [1]
        last = dist_pos[0]
        # for i, p in range(1, len(dist_pos)):
        #     if last == dist_pos[i]: group_dist_pos[-1]+=1
        #     else:#
        #         last = dist_pos[i]
        #         group_dist_pos.append(1)

        n_transition = len(set(dist_pos))
        n_char = len(set(w))
        # [start_char, [direction, shift, number]+]+
        # direction,#
        #     0 - same,#
        #     1,2..8 - U, UR, R, RD, D, DL, L, UL

        weight = float(n_transition)/len(dist_pos) + \
            float(len(w))/n_char
        seq_list = []
        if weight<1.3:
            seq = [w[0], [], self.isShift(w[0]), 0]
            for i in range(1,len(w)):
                is_shift_ = self.isShift(w[i])
                if not seq[1] and is_shift_==seq[2]:
                    seq[1] = dist_pos[i-1]
                    seq[3] += 1
                elif seq[1] != dist_pos[i-1] or seq[2] != is_shift_:
                    seq_list.append(seq)
                    seq = [w[i], [], is_shift_, 0]
                else:
                    seq[3]+=1
            if seq: seq_list.append(seq)
            for i,seq in enumerate(seq_list):#
                seq_list[i] = [seq[0], self.encode_keyseq(seq)]
        return weight, seq_list

# 专门处理日期的类
class Date:
    """
    Dt --> MDY, DMY, Y, MD, YMD, M/D/Y, D/M/Y
    Y --> yy | yyyy
    M --> mm | mon
    D --> dd
    mm --> 01 - 12
    dd --> 01 - 31
    mon --> Jan - dec
    yy --> [4-9][0-9] | [0-2][0-9]
    yyyy --> 19[4-9][0-9] | 2[01][0-9][0-9]
    """
    yy = '([6-9][0-9])'
    yyyy = '(19[4-9][0-9]|20[0-3][0-9])'
    mm   = '(0[0-9]|1[0-2])'
    mon  = '(jan | feb)' # TODO: Not sure how to handle this
    dd   = '([0-2][0-9]|3[01])'
    date_regex = re.compile(r"""^(?P<date>
(?P<mdy>{mm}{dd}{yy})|
(?P<mdY>{mm}{dd}{yyyy})|
(?P<dmy>{dd}{mm}{yy})|
(?P<dmY>{dd}{mm}{yyyy})|
(?P<y>{yy})|
(?P<Y>{yyyy})|
(?P<YY>{yyyy}{yyyy})|
(?P<md>{mm}{dd})|
(?P<ymd>{yy}{mm}{dd})|
(?P<Ymd>{yyyy}{mm}{dd})
)
$""".format(**{'mm': mm, 'yy': yy, 'yyyy': yyyy,
             'dd': dd}),
                            re.VERBOSE)
    # TODO: randomize the ordering of mm and dd,
    # Secuirty concern

    def __init__(self, word=None, T_rules=None):
        # self.date += "|(?P<mobno>\(\d{3}\)-\d{3}-\d{4}|\d{10}))\
        #              (?P<postfix>\D*$)"
        self.date = {}
        if word:
            self.set_date(word)
        if T_rules:
            self.update_date_regex(T_rules)

    def set_date(self, date_W):
        self.date = self.IsDate(date_W)

    def update_date_regex(self, T_rules):
        # customized Date regex
        regex = '^(?P<date>%s)' % \
                ('|'.join(['(?P<%s>%s)' % \
                           (r.replace(',',''),#
                            ''.join([self.regexes(x)
                                     for x in r.split(',')]))
                           for r in T_rules])
             )
        self.date_regex = re.compile(regex)

    def regexes(self, sym):
        D = {'m': 'mm',
             'y': 'yy',
             'Y': 'yyyy',
             'd': 'dd'}
        return eval('self.'+D[sym])

    def symbol(self):
        return 'T'

    def length(self, var):
        if var == 'Y': return 4
        elif var in ['m', 'd', 'y']: return 2
        else: return 99

    def encodeDate(self):
        return ''

    def parse_tree(self):
        print (self.date)
        return self.date

    def rule_set(self):
        r = RuleSet()
        comb = ''.join([x[0][-1] for x in self.date])
        r.add_rule('T', comb)
        for l in self.date:
            r.add_rule(*l)
        return r

    def IsDate(self, s):
        m = re.match(self.date_regex, s)
        if not m:
            return None
        m_dict = dict((k,v)#
                      for k,v in m.groupdict().items()#
                      if v and k!='date')#
        k, v = list(m_dict.items())[0]
        x = ParseTree()
        for l in k:
            x.add_rule(("T_%s"%l, v[:self.length(l)]))
            v = v[self.length(l):]
        return x

    def __deepcopy__(self, memo):
        return self

    def __nonzero__(self):
        return bool(self.date)
    __bool__ = __nonzero__

    def __str__(self):
        return str(self.date)

if __name__ == "__main__":
    # print GrammarStructure().getTermFiles()
    print (Date(T_rules=['Y,m,d'], word='20131026'))
