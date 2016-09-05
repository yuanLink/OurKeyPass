#   -*- coding:utf-8    -*-


#   Author:Link

import dawg

PINYINDIC = "pinyin.cfg"
PINYINDAWG = "pinyin.dawg"
PASSWORDDIC = "password_12306.cfg"

def countAllPinYin(filename):

    fp = open(filename,'r')
    wp = open(PINYINDIC,'w')
    a = set()
    for eachline in fp:

        line= eachline.strip().replace("    "," ").split(" ")

        for each in line[1:]:

            each = each[:-1]
            each+='\n'
            a.add(each.lower())

    for each in a:

        wp.write(each)

    wp.close()
    fp.close()

def staticAllPinYin(filename):

    fp = open(filename,'r')
    wp = open(PINYINDIC,'r',encoding ="utf-8")
    G = {}
    Key = {}
    for each in wp:
        each = each.strip().split(' ')
        try:
            G[each[0]] = G.get(each[1],0)
        except IndexError as e:
            G[each[0]] = 0

    wp.close()

    wp = open(PINYINDIC,'w')
    kp = open(PASSWORDDIC,'w')

    for eachline in fp:

        line = eachline.strip().split("----")
        
        #line1就是我们要的密码
        for each in G:
            if each in line[1]:
                G[each]+=1
        try:
            Key[line[1]] += 1
        except KeyError as  e:
            Key[line[1]] = 1
        
    fp.close()

    for each in G:

        wp.write("%s %d\n"%(each,G[each]))
    for each in Key:
        kp.write("%s %d\n"%(each,Key[each]))

    wp.close()
    kp.close()

def buildDAWG(filename):

    fp = open(filename,'r')

    my_list = []
    for each in fp:
        line = each.strip().split(' ')
        print(line)
        my_list.append((line[0],int(line[1])))

    my_dawg = dawg.IntDAWG(my_list)

    with open(PINYINDAWG,'wb') as f:
        my_dawg.write(f)

if __name__ == "__main__":
    #countAllPinYin("word.data")
     staticAllPinYin('12306.txt')


        