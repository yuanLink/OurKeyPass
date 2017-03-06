#   -*-coding:utf-8 -*-


__author__ = 'Link'

import re
import bz2
import json
from collections import OrderedDict
from dawg import IntDAWG,DAWG
from helper import open_,convert2group,whatchar,print_once,bin_search
from lexer_helper import Date,ParseTree
from lexer_01 import NonT_L, get_nont_class
from honeyvault_config import RULE_PATH
import random 


PASSWORD_MAX_LENGTH = 32


class Grammer(object):
    """
    功能：处理pcfg加密和解密的类
    属性：
    G OrderedDict：存放各种规则
    l33t_replace：各类可替换规则

    方法：
    parse：分析密码的组成内容s
    """

    G = ''
    l33t_replaces = DAWG.compile_replaces({
            '3':'e', '4':'a', '@':'a',
            '$':'s', '0':'o', '1':'i',
            'z':'s'
    })

    def __init__(self,filename,cfg = False):

        self.cal_cdf = cfg
        self.load(filename)
        self.Non_set = []
        for each in self.G:
            # 不能有_存在G中
            if each.find('_')<0:
                self.Non_set.append(each)


    # 读入字典，并且统计所有的规则的sym
    def load(self,filename):
        self.G = json.load(open_(filename),object_pairs_hook = OrderedDict)
        # 这里读取字典的键值
        for k,v in self.G.items():
            if self.cal_cdf:
                # print_err("Calculating CDF!")
                # lf表示的是当前规则中的数量
                # 每一个规则都要把上一次的规则的数量加载其中（有点像是处理（5）-（0）就能求出从1~5的规则出现的次数
                lf = 0
                for l,f in v.items():
                    # v[l] += lf
                    lf += f
                v['__total__'] = lf
            else:
                v['__total__'] = sum(v.values())

        # 然后这里统计出现的所有的W字符串，在一会得字符串生成过程中使用
        self.Wlist = []
        for k,D in self.G.items():
            if k.startswith('W'):
                self.Wlist.extend([x for x in D])

        # 设定data变量，方便管理日期规则
        self.date =Date()
        # 建立dawg，方便生成管理word规则
        self.Wlist = IntDAWG(self.Wlist)

    # 产生一个（sym,([word]).prod)的规律
    def getProb(self,l,r):
        f = self.G.get(l,{}).get(r,0)
        return max(float(f)/self.G[l]['__total__'],0.0)


# 方法：得到最可能符合密码的规则
# 返回值：list，内部存有类似于节点的点
# 其中：
# 如果为word类型，则返回值定义为('W1',[(similar_keys,Nont_T)],prob)
# 如果为time类型，则返回值定义为('T',[(passwd,Date)],prob)]
# 否则返回值定义为(sym,[(passwd)],prob)


    def genRuleMatches(self,passwd):

        # 用于存储所有可能的规则
        l = []
        # 首先要查找这段密码属于哪个规则：
        for rule in self.Non_set:
            # =================如果是词汇规则的话============================
            if rule.startswith('W'):
                # 在之前整理的dawg中查找
                k = self.Wlist.similar_keys(passwd.lower(),self.l33t_replaces)
                # 将最相似的作为规则
                if k:
                    sym = "W%s"%(get_nont_class('W',passwd))
                    prod = NonT_L(k,passwd)
                    prob = self.getProb(sym ,passwd.lower())
                    l.append((sym,[(k[0],prod)],prob))
            # ================如果是时间规则的话=============================
            elif rule.startswith('T'):
                # 在之前找到的Date中处理passwd,
                # 假如是日期的话，返回值[('T_Y', '2013'), ('T_m', '10'), ('T_d', '26')]类似
                T = self.date.IsDate(passwd)
                if T:
                    sym = 'T'
                    prod = (passwd,T)
                    prob = 10**(len(passwd)-8)
                    for each in T:
                        prob *= self.getProb(*each)
                    # print((sym,[prod],prob))
                    l.append((sym,[prod],prob))
                # 如果不是这两个种类的话，其他种类的规则是没有节点的
            else:
                # 只需要计算出现概率即可
                f = self.G[rule].get(passwd,0)
                if f>0:
                    l.append((rule,[(passwd)],float(f)/self.G[rule]['__total__']))

        # 然后我们查找，把概率最高的规则作为返回值
        temp_prob = 0;tu = ()
        for each in l:
            if temp_prob< each[2]:
                tu = each
                temp_prob = each[2]

        return tu           

    def not_startswith_L_T(self,passwd):
        if passwd:
            if passwd[0].startswith('L_') or passwd[0].startswith('T_'):
                return False
            else:
                return True
        else:
            return passwd



# 方法：把两个不同的节点连接起来


    def join(self,l,r):
        # 如果不是特使的节点就把它们连起来
        if self.not_startswith_L_T(l) and self.not_startswith_L_T(r):

            sym = ','.join([l[0],r[0]])
            prob = l[-1]*r[-1]
            prod = l[1] + r[1]

            return (sym,prod,prob)

    def parse(self,passwd):

        # 首先检验读入的字符串不是空字符串
        if not passwd:
            return ''

        nonTRule = {}

        # 然后是对读入的字符串进行分析
        # 使用它的算法：先算每一个叫部分的规则，然后组合起来（有点像。。。。那个。。分治的思想）
        index = 0
        first = True
        for rep in range(len(passwd)):
            for start in range(len(passwd) - rep):
                index += 1
                # 1、（分）将字符串分成不同的小块进行分析（治）,得到此部分的方法
                # (此处思想是二维的动归,rep表示的是此时跨过多少个字符串)

                # nonTRule[(start,start+rep)] = self.genRuleMatches(passwd[start:start+rep+1])
                non = self.genRuleMatches(passwd[start:start+rep+1])
                if first:
                    print(non)
                    first = False
                rule_list = []
                rule_list.append(non)

                # 2、（合）分析各个部分的小块的发生概率，分别记录下来
                for bet in range(start,start+rep):

                    temp_non = self.join(nonTRule[(start,bet)],nonTRule[(bet+1,start+rep)])
                    rule_list.append(temp_non)

                # 3、（计）找到发生概率最大的规则，将这个规则当作此时[start：start+rep+1]的值
                # 使用fliter生成迭代对象，更好找我们要的变量prob
                # temp = filter(lambda k:k,rule_list)

                # 记录下此时的最可能的规则
                if rule_list:
                    nonTRule[(start,start+rep)] = max(rule_list, key = lambda x: x[-1] if x else 0)
                    # print(nonTRule[(start,start+rep)])
                else:
                    nonTRule[(start,start+rep)] = ()
                
                
        print("in the pares it print ",end = '')
        print(nonTRule[(0,len(passwd) -1)])
        return nonTRule[(0,len(passwd) -1)]

    # 简单解析函数，将简单规则的密码进行加密（这个简单规则是指类似于123456）或者无法解释的内容
    def defaultPasswordParse(self,word):
        # 将所有的密码格式设置成G -> W1,G | D1,G | Y1,G | W1 | D1 | Y1的形式
        pt = ParseTree()
        print("default password parse is ",end = '')
        print(pt)
        n = len(word)
        for i,c in enumerate(word):
            r = whatchar(c) + '1'
            # if i<n-1:
            #     r = r + ',G'
            pt.add_rule(('G', r))
            pt.add_rule((r[:2], c.lower()))
            if r.startswith('W'):
                nont_l = NonT_L(c, c)
                pt.extend_rules(nont_l.parse_tree())

        return pt
        # 简单规则中，其实也差不多，就是直接看是


    # 解析函数，目的是将函数解析成需要的语法树，然后在cfg中查找需要的值
    def lParseTree(self,passwd):

        pt = ParseTree()

        rule = self.parse(passwd)
        print("our rule is ")
        print(rule)

        # 如果返回值为空的话，则说明翻译失败。记录此时密码
        if not rule:
            print("Failed encode %s"%passwd)
            return pt

        # 假如是无G状态，就是说简单的密码时，就使用简单的密码加密
        if rule[0] not in self.G['G']:
            return self.defaultPasswordParse(passwd)

        # 否则的话，首先设定第一层的规则
        pt.add_rule(('G',rule[0]))

        # 然后，将每一层规则和每一个内容读出来，安插到parsetree中

        for sym, rhs in zip(rule[0].split(','), rule[1]):

            # 首先确认一下，假如规则不是W或者T的话，rhs此时应该只是字符串
            if isinstance(rhs, str):
                # 然后可以直接把这个规则放入
                pt.add_rule((sym, rhs))

            # 假如这个规则是W的话，那么后面跟着的就是(similarkeys_list,NonT_L)则此时要记得先把最相似对象内容放入存档中，并且记录下此时的内容大小写状态
            elif sym.startswith('W'):

                pt.add_rule((sym, rhs[0]))
                # 这里使用parse_tree变量，把此时的单词的状态子叶记录
                ltree = rhs[1].parse_tree()
                # 然后，此时先把最初的规则放进去
                pt.add_rule(ltree[0])
                # 假如此时为’133t'规则的话，此时在'133t'之后会记录下此时可能发生替换的元素，则要把这些元素也放入(这些元素已经打包好了)
                if len(ltree)>1:
                    pt.tree.extend(ltree[1][1])
            # 假如规则是T的话，那么肯定是('T',[('T_Y','1993')..]..)之类的
            elif sym.startswith('T'):
                # 为了与cfg文件内部保持一致，我们此时需要把文件转换成与cfg内的文件一致的格式
                temp_sym = ''
                for each_label in rhs[1]:
                    temp_sym += each_label[0].replace("T_","")
                pt.add_rule((sym, temp_sym))

                # 然后把其他的节点也放进去
                pt.extend_rules(rhs[1])

            else:
                print("we can't figure out this word")

        # 完成
        return pt


    # 核心加密函数：用于替换我们的密码
    def encode_password(self, password):
        # 首先得到我们的密码的密码树
        ptree = self.lParseTree(password)
        print("our password is ",end = '')
        print(ptree)
        if not ptree:
            print("encode failed,change")
        # 然后将这个密码树映射到不同的数字中：
        encd = []
        # print(ptree)
        for each_node in ptree:
            try:
                encd.append(self.encode_encd(*each_node))
                # print(encd)
            except ValueError as e:
                print("Error in encoding: \"{}\"".format(password))
                print(e)
                return []

        # 假如不出错的话此时就完成了加密，然后注意此时我们的密码可能没有填充完（因为密码本身过短，我们需要使用空白值来填充）
        length = PASSWORD_MAX_LENGTH - len(encd)

        # 此时，如果length的长度还是len（encd），那么说明加密失败，返回空列表
        if length == PASSWORD_MAX_LENGTH:
            return []

        for i in range(length):
            encd.append(convert2group(0, 1))

        # 映射完成,返回加密完成的数字
        return encd

    # 比例加密函数，用于在一个固定额度区间中获得一个随机数
    def encode_encd(self,l,r):
        # 临时字典，存储此l规则对应的值

        rhs_dict = self.G[l]
        # print(rhs_dict[r])
        # 然后获得r的下标
        i = list(rhs_dict.keys()).index(r)
        # 然后开始循环，将其之前的数字进行相加
        l_hs = 0
        r_hs = 0
        for each_index in range(i):
            l_hs += list(rhs_dict.values())[each_index]
        # 然后记录下随机数的右侧
        r_hs = l_hs+ rhs_dict[r]-1

        # 最后调用随机函数，生成介于两者之间的随机数(这里记得把最大值也放上)
        rn = random.randint(l_hs,r_hs)
        # print("l_hs is %d,r_hs is %d and the random is %d"%(l_hs,r_hs,rn))
        # wn = rn + random.randint(0, int((3000000-rn)/rhs_dict['__total__'])) * rhs_dict['__total__']
        wn = convert2group(rn,rhs_dict['__total__'])
        # print("the wn is %d and it come back is %d"%(wn,wn%rhs_dict['__total__']))
        return wn

    # 比例解密函数
    def decode_encd(self,l,r):
        # 临时字典，存储此时l规则对应的值
        rhs_dict = self.G[l]
        # 然后此时检擦一下是否储存在这个规则（虽然一般都有，可能反解码的时候没有（？）
        if not rhs_dict:
            return ''
        # 还要确保__total__这个属性一定要有，否则就GG
        assert '__total__' in self.G[l] ,"The __total__ was lost in {!r},l = {!r}"\
            .format(rhs_dict,l)

        # 然后可以开始计算这个值得位置：
        index = r%rhs_dict['__total__']
        # print("the r is %d ,index is %d"%(r,index))
        # 接下来，判断参数，决定查找方式
        # if self.cal_cdf:
        #     # 假如这个规则比较大的话，我们顺便记录一下这个映射（不知道是否有必要）是否输出
        #     if len(rhs_dict)>1000:
        #         print_once(l,len(rhs_dict))
        #     # 使用二分搜索快速查找
        #     return bin_search(list(rhs_dict.items()),index,0,len(rhs_dict))

        # 未使用参数的话，使用比较慢的查找方式
        for k, t in rhs_dict.items():

            if index<t:
                return k
            else:
                index-=t 

        # 到达这里，说明没有找到。。。检查一下输入是什么吧
        print("not find the rule !l is %s and r is %d"%(l,r))
        return ''


        # 尝试进行解密
    def decode_password(self,passwd):
        """
        函数：解密加密的随机串
        作用：通过取余运算，将每一个数字对应的原来的法则进行还原，同时利用G点找到之前加密过的密码位置，依次解密
        重要参数作用：
        stack：存放存入的节点
        plaintext：存放解密后的字符串
        lhs：存放父节点，父节点上存放了某种规则，必定不是字符串
        rhs：存放子节点，可能是下一个元素的子节点，可能是字符串
        """

        if not passwd:
            return ''

        # 解密的过程有点像栈堆一样
        # 首先新建一个list（如果成功了就换成stack)
        stack = []
        # 然后放入第一个节点（一定是这个，及即时是无法找到对应规则的我们也有G节点）
        stack.append('G')

        plaintext = ''

        index = 0
        # 然后进行循环，将密码进行解析
        while len(stack)>0:
            lhs = stack.pop()
            # 使用读取功能，检测当前的nond，然后返回当前的状态值
            rhs = self.decode_encd(lhs,passwd[index])
            index+=1
            # 检查此时的rhs节点情况
            # 假如该节点为普通节点（而不是什么T_y,L_s那种）
            if lhs in ['G','Y','R','D','T','W']:
                # 那么节点后跟着的就是内容了
                if lhs == 'T':
                    # !!可能出错！！
                    sym = ['T_%s'%c for c in rhs]
                # 普通节点后面跟着的就是普通的规则，用‘，’作为分割符把其分开
                else:
                    # print("the rhs is %s"%rhs)
                    sym = rhs.split(',')
                # 无论哪种情况，都需要把内容颠倒过来（因为放到栈里面，后进先出）
                sym.reverse()
                # 然后放入栈中
                stack.extend(sym)
            # 假如此时节点已经是字符节点了，则此时右侧的字符串还未完全的还原，此时还需要把部分元素替换，使用特殊的函数还原
            elif lhs.startswith('W'):
            # 这里passwd放进去，因为下一位必定是大小写判断
                l = self.decode_encd('L',passwd[index])
                index+=1
            # 然后此时判断类型
                if l =="lower":
                    plaintext+=rhs
                elif l == "Caps":
                    plaintext+=rhs.capitalize()
                elif l == "UPPER":
                    plaintext+=rhs.upper()
            # 假如是l33t，则此时每个符号都进行了加密，将每个符号进行解密
                elif l == "l33t":

                   for c in rhs: 
                    plaintext+=self.decode_encd('L_%s'%c,passwd[index])
                    index+=1
            # 否则，此时已经是最终节点了
            else:
                plaintext+=rhs

        return plaintext


if __name__ == "__main__":

    g = Grammer(RULE_PATH + "temp2.bz2",True)
    temp = g.encode_password("wyz123123")
    print(g.decode_password(temp))

    
