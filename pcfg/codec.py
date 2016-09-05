#   -*-coding:utf-8 -*-


from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex,a2b_hex

def encode(num):
    code = []
    while num:
        code.append(num%256)
        num = int(num/256)
    code.reverse()

    return bytes(code)


def decode(code):
    num = 0
    for c in code:
        num = num*256 + c

    return num


def DTE_AES_encode(passwd, key, mode = AES.MODE_ECB):
    """
    用于对用户密码进行aes加密的函数。
    
    如果使用定长的加密模式，我们会在passwd最后添加！作为结尾符，再在最后添加0，填充满16的倍数

    :Parameters:
    @param passwd：用于加密的函数
    @param key：主密钥
    @param mode = AES.MODE_CBC
    
    :Return: 一个加密完成的byte类型的数据
    """

    iv = Random.new().read(AES.block_size)

    if mode == AES.MODE_CBC:
        crypto = AES.new(key, mode, iv)
        
    elif mode == AES.MODE_ECB:
        crypto = AES.new(key, mode)

    length = len(passwd)

    if length%16 != 0:
        x = length%16
        passwd = passwd + "!" + (16-x-1)*'0'
        de = crypto.encrypt(passwd)
        
    return de

def DTE_AES_decode(passwd, key, mode = AES.MODE_ECB):
    """
    用于对用户密码进行aes解密的函数。

    :Parameters:
    @param passwd：用于加密的函数
    @param key：主密钥
    @param mode = AES.MODE_CBC：加密的模式
    
    :Return: 一个解密后的字符串    
    """
    iv = Random.new().read(AES.block_size)

    if mode == AES.MODE_CBC:

        crypto = AES.new(key, mode, iv)
        de = crypto.decrypt(passwd)
        
        # return a2b_hex(d) 
    elif mode == AES.MODE_ECB:

        crypto = AES.new(key, mode)
        de = crypto.decrypt(passwd)

    de = de.decode().rstrip('0')

    return de[:-1]

if __name__ == '__main__':

    key = '1234567890abcdef'
    
    print(DTE_AES_decode(DTE_AES_encode('123123', key), key))
