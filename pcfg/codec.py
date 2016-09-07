#   -*-coding:utf-8 -*-
# import sys
# print(sys.path)
# from binascii import b2a_hex,a2b_hex
from Crypto.Cipher import AES
from Crypto import Random
import ourPcfg


class PcfgEncode(object):
    """
    用于处理整个pcfg加密的类。

    类中有两个函数，分别用于加密的和解密
    """

    def __init__(self, key, filename='temp2.bz2'):
        """
        打开规则集，并记录主密钥

        :Parameter:
        @param key str:用户输入主密钥
        @param filename str:训练集，必须是.bz2文件

        """

        self.g = ourPcfg.Grammer(ourPcfg.RULE_PATH + filename, True)
        self.key = key

    def encode(self, num):
        code = []
        while num:
            code.append(num % 256)
            num = int(num/256)
        code.reverse()

        return bytes(code)

    def decode(self, code):
        num = 0
        for c in code:
            num = num*256 + c

        return num

    # TODD:等大部分功能完成再来完善吧。。
    def DTE_AES_encode(self, passwd, mode=AES.MODE_ECB):
        """
        用于对用户密码进行aes加密的函数。
        
        如果使用定长的加密模式，我们会在passwd最后添加！作为结尾符，再在最后添加0，填充满16的倍数
        :Parameters:
        @param passwd：用于加密的函数
        @param mode = AES.MODE_CBC
        :Return: 一个加密完成的byte类型的数据
        """
        iv = Random.new().read(AES.block_size)

        if mode == AES.MODE_CBC:
            crypto = AES.new(self.key, mode, iv)    
        elif mode == AES.MODE_ECB:
            crypto = AES.new(self.key, mode)
        else:
            print("error")
            return ''

        length = len(passwd)
        if length%16 != 0:
            x = length % 16
            # print(passwd)
            passwd = passwd + b"!" + bytes((16-x-1)*'0', 'utf-8')
            # print(len(passwd))
            de = crypto.encrypt(passwd)
            
        return de

    def DTE_AES_decode(self, passwd, mode=AES.MODE_ECB):
        """
        用于对用户密码进行aes解密的函数。
        :Parameters:
        @param passwd：密文
        @param mode = AES.MODE_CBC：加密的模式
        :Return: 一个解密后的字符串    
        """
        iv = Random.new().read(AES.block_size)

        if mode == AES.MODE_CBC:

            crypto = AES.new(self.key, mode, iv)
            de = crypto.decrypt(passwd)
            
            # return a2b_hex(d) 
        elif mode == AES.MODE_ECB:
            crypto = AES.new(self.key, mode)
            de = crypto.decrypt(passwd)

        # print(de)
        de = de.rstrip(b'0')

        return de[:-1]

    # 封装函数，用于读入密码，并且将其进行加密
    def pcfg_encode(self, password):
        """
        读入传入的password，进行pcfg混淆后，然后对每一位进行加密。
        :Parameters:
        @param passwd：用于加密的函数
        :Return:
        一个list，里面放了32个加密后的bytes串
        如果发生错误，会返回一个空的列表
        """
        if len(password)>32 or len(password)<=5:
            print("password length is %d"%len(password))
            return []
        self.key = self.key.zfill(32)
        # print("in the pcfg_encode,the password is "+password)
        # 对密码进行pcfg混淆        
        temp_list= self.g.encode_password(password)
        # print(temp_list)
        # 然后对整个list进行处理
        encode_list = [self.encode(x) for x in temp_list]
        # print(encode_list)
        return [self.DTE_AES_encode(x) for x in encode_list]

    # 解码函数，将密码还原
    def pcfg_decode(self, passwd_list):
        """
        读入传入的password，进行pcfg混淆后，然后对每一位进行加密。
        :Parameters:
        @param passwd_list：list，加密后的东东
        :Return:
        一个string，为普通的密码
        如果发生错误，会返回一个空的字符串
        """
        if len(self.key)>32:
            return ''
        self.key = self.key.zfill(32)
        temp_list = [self.decode(self.DTE_AES_decode(x)) for x in passwd_list]
        # 传入列表，进行返混淆
        plaintext = self.g.decode_password(temp_list)

        return plaintext


if __name__ == '__main__':

    key = '1234567890abcdef'
    g = PcfgEncode(key)
    t = g.pcfg_encode('password')
    g = PcfgEncode('1234567890bbcdef')
    print(g.pcfg_decode(t))
