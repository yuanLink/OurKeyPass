# -*- coding: utf-8 -*-
import re
import bz2

from lexer_helper import ParseTree, Date, RuleSet
from dawg import IntDAWG, DAWG
from honeyvault_config import GRAMMAR_PATH
# !!ParseTree:语法树类，用于解析语法，并且存储语法：
# Date:日期类，在解读数字结构的时候使用
# KEyboard:键盘类，在解读接盘结构时候使用
# RuseSet:（基础）规则了类，用Ruleset来记录规则

NonT_length2classmap = {
    "W": {"1": [1, 2], "2": [3, 3], "3": [4, 4], "4": [5, 5], "5": [6, 6],# 
          "6": [7, 7], "7": [8, 8], "8": [9, 9], "9": [9, 30]},
    "D": {"1": [1, 1], "2": [2, 3], "3": [4, 6], "4": [7, 9], "5": [10, 30]},
    "Y": {"1": [1, 1], "2": [2, 30]}
    }

# nt ：需要分析的类型
# word ：待分析的字符串长度


def get_nont_class(nt, word):
    A = NonT_length2classmap.get(nt, {})
    n = len(word)
    for k, v in A.items():
        if n >= v[0] and n <= v[1]:
            return k


class NonT(object):  # baseclass
    """docstring for NonT"""
    def __init__(self):
        self.prob = 0.0
        self.prod = ''
        self.sym = ''

    def symbol(self):   # 返回标签
        return self.sym

    def probability(self):  # 返回规则概率
        return self.prob

    def production(self):   # 返回当前规则下，字符串
        return self.prod

    def __str__(self):  # 返回当前函数的规则及规则所对应的字符串
        p_str = [str(p) for p in self.prod] if isinstance(self.prod, list) else self.prod
        return '%s: %s (%g)' % (self.sym, p_str,self.prob)

    def parse_tree(self):
        p_tree = ParseTree()
        if isinstance(self.prod, basestring): # 单纯字符串则返回字符串，这里其实可以看成只有一个根节点的语法树
            return self.prod
        elif isinstance(self.prod, list):     # 是一个list，则将list中的每一个读出，添加后生成成一棵语法树
            for p in self.prod:
                p_tree.add_rule((p.sym, p.parse_tree()))
        else:                                 # 这是一个语法树，不用做任何处理了，直接看语法树内的节点是否还能生成语法树
            return self.prod.parse_tree()
        return p_tree

    def rule_set(self):   # 添加规则
        rs = RuleSet()
        if isinstance(self, NonT):    # 基础规则  即没有任何规则
            rs.add_rule('G', self.sym)
        if isinstance(self.prod, str):
            rs.add_rule(self.sym, self.prod)
        elif isinstance(self.prod, list):
            for p in self.prod:
                rs.update_set(p.rule_set())
        else:
            return self.prod.rule_set()
        return rs

    def __nonzero__(self):
        return bool(self.prod) and bool(self.prob)
    __bool__ = __nonzero__


class NonT_L(NonT):  # 特别注意 :这个类的作用是对NonT_W的概率进行修正，并不对NonT_W.prod修正。
    sym, prod, prob = 'L', '', 0.0

    def __init__(self, v, o_w):
        self.prod = 'l33t' if not o_w.isalpha() \
            else 'Caps' if o_w.istitle()  \
            else 'lower' if o_w.islower() \
            else 'UPPER'
        self.r = o_w  # origin_word原password
        self.l = v  # vocabulary 词表即进行解规则后的password
        if self.prod == 'l33t':
            c = len([c for c, d in zip(self.l, self.r)
                     if c != d.lower()])
            self.prob = 1 - c / len(self.r)
            # print("sucess") 测试用代码 T_T
        else:
            self.prob = 1.0
    # def parse_tree(self):
    #     p_tree = ParseTree()
    #     p_tree.add_rule(('L', self.prod))
    #     L = ['L_%s' % c for c in self.l]
    #     if self.prod == 'l33t':
    #         p_tree.add_rule(('l33t', zip(L, self.r)))
    #     return p_tree

    # def rule_set(self):
    #     rs = RuleSet()
    #     rs.add_rule('L', self.prod)
    #     if self.prod is 'l33t':
    #         for c,d in zip(self.l, self.r):
    #             rs.add_rule('L_%s'%c,d)
    #     return rs

    def __str__(self):
        return "NonT_L: ({}, {})".format(self.l, self.r)
        # return "%s <%s> " % (self.l,self.r)


class NonT_W(NonT):
    sym, prod, prob = 'W', '', 0.0
    english_dawg = IntDAWG().load(GRAMMAR_PATH + 'words.dawg')
    chinese_dawg = IntDAWG().load(GRAMMAR_PATH + 'pinyin.dawg')
    total_f = english_dawg[u"__total__"] + chinese_dawg[u'__total__']
    # thisdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # word_dawg  = IntDAWG().load('{}/data/English_30000.dawg'.format(thisdir))
    # fname_dawg = IntDAWG().load(
    #     '{}/data/facebook-firstnames-withcount.dawg'.format(thisdir))
    # lname_dawg = IntDAWG().load(
    #     '{}/data/facebook-lastnames-withcount.dawg'.format(thisdir))
    # total_f = word_dawg[u'__total__'] + \
    #     fname_dawg[u'__total__'] + \
    #     lname_dawg[u'__total__']
    l33t_replaces = DAWG.compile_replaces({
            '3': 'e', '4': 'a', '@': 'a',
            '$': 's', '0': 'o', '1': 'i',
            'z': 's'
            })

    def __init__(self, word):
        # 传入参数为待分析的密码
        # super(NonT_W, self).__init__()
        w = word.lower()
        dawg = []
        for d in [self.english_dawg,self.chinese_dawg]:
            # 使用replaces的替换，找到和w相似的内容，返回一个list，【0】为与w最相似的部分
            k = d.similar_keys(w, self.l33t_replaces)
            if k:
                dawg.append((d, k[0]))
        # dawg中存放了之前word,fname,lname中与密码最相似的部分
        if dawg:
            # d[1]中存放的是word，fname，lname；里面的字符串可能会有重复的地发
            v = list(set([d[1] for d in dawg]))
            # 假如这个v中存在两个以上的字符串，或者说第一个元素不全是字符串（？？？会这样的咩）
            if len(v) > 1 or not v[0].isalpha():
                return  #
            # 这里说明，这个字符串至少出现过一次，这里在不同的字典中统计这个字符串的出现次数
            v = v[0]
            f = sum([d[0][v] for d in dawg])

            self.prod = v
            self.sym = 'W%s' % get_nont_class('W', v)

            self.L = NonT_L(v, word)    # 引入NonT_L 分析password的大小写情况
            # print(self.L)
            self.prob = self.L.prob * float(f)/self.total_f # 添加特殊字符对概率的影响
    # def parse_tree(self):
    #     pt = ParseTree()
    #     pt.add_rule((self.sym, self.prod))
    #     pt.extend_rules(self.L.parse_tree())
    #     return pt
    # def rule_set(self):
    #     rs = RuleSet()
    #     rs.add_rule(self.sym, self.prod)
    #     rs.update_set(self.L.rule_set())
    #     return rs

    def parse_tree(self):
        pt = ParseTree()
        pt.add_rule((self.sym, self.prod))
        pt.extend_rules(self.L.parse_tree())
        return pt

    def rule_set(self):
        rs = RuleSet()
        rs.add_rule(self.sym, self.prod)
        # rs.update_set(self.L.rule_set())
        return rs

    def __str__(self):
        return '%s: %s<%s> (%g)' % (self.sym, self.prod,self.L,
                                    self.prob)


# combine 节点：把其他节点合并成一个（就像是把树的子节点整合成一个大的节点）所以这里的prod是其他节点的list结合，而sym是简单的字符串连接
class NonT_C(NonT):
    sym, prod, prob = 'C', '', 1.0
    # 传入的参数是nonset（节点tuple），里面放的是各个节点

    def __init__(self, *nonset):

        for eachNon in nonset:
            # 保证每一个节点都不是空节点
            if not eachNon:
                return  #
        # 结合sym(会形成例如"D1,D3,E8"这类)
        self.sym = ','.join([eachNon.sym for eachNon in nonset])
        self.prod = []
        # 结合prod(将不同的production放在同一个list里面),同时计算概率
        for eachNon in nonset:
            if isinstance(eachNon.prod ,list):
                self.prod.extend(eachNon.prod)

            else:
                self.prod.append(eachNon)

            self.prob = self.prob*eachNon.probability()


class NonT_D(NonT):
    ''' 数字规则类'''
    sym, prod, prob = 'D', '', 0.0# 

    def __init__(self, w):
        if w.isdigit():
            self.prod = w
            self.prob = 0.001
            self.sym = 'D%s' % get_nont_class('D', w)
        d = Date(w)
        if d:
            self.sym = 'T'
            self.prod = d
            self.prob = 10**(len(w)-8)

    def parse_tree(self):
        if isinstance(self.prod, str):
            return ParseTree(self.sym, self.prod)
        else:
            return self.prod.parse_tree()

    def rule_set(self):
        if isinstance(self.prod, str):
            return RuleSet(self.sym, self.prod)
        else:
            return self.prod.rule_set()


class NonT_Y(NonT):
    """特殊字符规则类"""
    sym, prod, prob = 'Y', '', 0.0# 
    regex = r'^[\W_]+$'

    def __init__(self, w):
        if re.match(self.regex, w):
            self.prob = 0.01
            self.prod = w
            self.sym = 'Y%s' % get_nont_class('Y',w)


class NonT_R(NonT):
    """重复规则类"""
    sym, prod, prob = 'R', '', 0.0

    def __init__(self, w):
        x = len(set(w))/float(len(w))
        if x < 0.2:
            self.prob = 1 - float(x)/len(w) # 这个概率计算方法是值得推敲的，但是我暂时无法反驳这种计算方法
            self.prod = w


# !!ParseTree:语法树类，用于解析语法，并且存储语法：
# Date:日期类，在解读数字结构的时候使用
# KEyboard:键盘类，在解读接盘结构时候使用
# RuseSet:（基础）规则了类，用Ruleset来记录规则


"""
规则定义：
W：字符，分为<英语单词>+L
W -> <english-word>L | <name>L

D：数字，可能为<date>日期类|<phone-no>电话类（？）|随机数字
D -> <date> | <phone-no> | [0-9]+

Y：符号，除了数字和字母以外的所有字符
Y -> [^\W]+  # symbol

K：键盘键盘位置，是我们人为定义的规则种类
K -> <keyboard-sequence>

R：重复，通过查看之前的
R -> repeat

S：连续值（？）
S -> sequence # 123456, abcdef, ABCDEFG

L：字符子类，对字符的大小写|l33t继续分类
L -> Capitalize | ALL-UPPER | all-lower | l33t

G：组合类，将之前的规则进行组合
G -> <some-combination-of-those-NonTs>
"""

"""
函数：得到NonT（规则节点）
功能：找出passwd在我们定义的可能的方法类中最可能的一类
参数定义：
rule_list list:定义了需要进行分析的代码段
返回值：
某个NonT_类
"""


def getGenNonT(passwd):

    # 检查一下传入的参数免得爆炸
    if not passwd:
        return ''

    # 然后测试这个passwd到底是哪个规则
    rule_list = [NonT_W, NonT_R, NonT_D, NonT_Y]

    # 同样使用filter，将结果定义为迭代对象）等一下可以直接用max把最大
    # t = filter(lambda x:x,[rule(passwd) for rule in rule_list])

    # return max(t ,key = lambda x:x.probability())
    prob = 0.0
    maxNonT = ''
    for eachRule in rule_list:
        tempNonT = eachRule(passwd)
        if prob <= tempNonT.probability():
            prob = tempNonT.probability()
            maxNonT = tempNonT

    return maxNonT

"""
函数：解析字符串（概率）
功能：将一串输入的字符串解析成一个概率最高的规则型式
参数定义：
nonTRule dict ：记录下从第start到第end的规则（可能为NontC也可能为其他）
rule_list list: 临时变量，记录下从第start到第start+rep之间可能的所有规则
start int：记录下此时的变量起点
rep int：记录下此时的变量重点
返回值：返回一个NonT_C的节点，表示开头（？）
"""


def parse(passwd):

    # 首先检验读入的字符串不是空字符串
    if not passwd:
        return ''

    # 使用了一个类字典，存储整个字符串分析的时候每段对应的规则
    # 例如"pass" nonTRule = {(0,0):0.001,(0,1):0.1}这里的意思是'p'概率为0.001，'pa'概率为0.1
    nonTRule = {}

    # 然后是对读入的字符串进行分析
    # 使用它的算法：先算每一个叫部分的规则，然后组合起来（有点像。。。。那个。。分治的思想）
    index = 0
    # first = True
    for rep in range(len(passwd)):
        for start in range(len(passwd) - rep):
            index += 1
            # 1、（分）将字符串分成不同的小块进行分析（治）,得到此部分的方法
            # (此处思想是二维的动归,rep表示的是此时跨过多少个字符串)

            non = getGenNonT(passwd[start:start+rep+1])

            rule_list = []
            rule_list.append(non)

            # 2、（合）分析各个部分的小块的发生概率，分别记录下来
            for bet in range(start, start+rep):
                temp_non = NonT_C(nonTRule[(start, bet)],
                                  nonTRule[(bet+1, start+rep)])
                rule_list.append(temp_non)

            # 3、（计）找到发生概率最大的规则，将这个规则当作此时[start：start+rep+1]的值
            # 使用fliter生成迭代对象，更好找我们要的变量prob
            temp = filter(lambda k:k,rule_list)

            # 记录下此时的最可能的规则
            nonTRule[(start, start+rep)] = max(temp,
                                               key=lambda k:k.probability())

    # for each in nonTRule:
    #   print(nonTRule[each])
    # 在完成所有的分析后，最后再把这个节点包装（？）
    return NonT_C(nonTRule[(0, len(passwd) -1)])

"""
函数：pcfg训练函数
功能：将
参数定义：
filename :用于存放训练集的位置
rule_set：存放规则以及其频率的类
"""


def buildOurpcfg(filename):

    # 准备好用于存放规则的类
    rule_set = RuleSet()

    # 然后打开文件
    fp = open(filename, 'r')

    # 设定最大的可读取行数
    max_line = 25550

    for i, line in enumerate(fp):
        if i > max_line:
            break

        # 开始进行检测(规定第一个是密码，第二个是出现次数)
        line, n = line.strip().split(' ')

        p = parse(line)

        # 设置规则
        rule_set.update_set(p.rule_set(),with_freq = True,freq = int(n))

    # 完成训练，进行存档

    rule_set.save(bz2.BZ2File("temp1.cfg","wb"))

    buildOurpcfg("password_12306.cfg")


if __name__ == "__main__":

    print(parse("Pass"))
