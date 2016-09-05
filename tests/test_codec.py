# coding: utf-8

import unittest
import os,sys
sys.path.append(os.path.abspath(os.path.pardir))
from pcfg import codec


class TestCodec(unittest.TestCase):
    def setUp(self):
        self.number = 1653522623
        self.key = '1234567890abcdef'
        self.code = b'b\x8e\xc0\xbf'
        self.aes_encode = b'\xb5\x8d\xf1\x0f\xfc\x0b6\xebq\x99\xb7_=\xc7\x82R'
        self.aes_decode = '123123'

    def tearDown(self):
        pass

    def test_encode(self):
        code = codec.encode(self.number)
        self.assertEqual(code, self.code)

    def test_decode(self):
        number = codec.decode(self.code)
        self.assertEqual(number, self.number)

    def test_dte_encode(self):
        num_encode = codec.DTE_AES_encode(self.aes_decode, self.key)
        self.assertEqual(num_encode, self.aes_encode)

    def test_dte_decode(self):
        num_deocde = codec.DTE_AES_decode(self.aes_encode, self.key)
        self.assertEqual(num_deocde, self.aes_decode)        

if __name__ == '__main__':
    # __import__("sys").argv.append("-v")         # 采用verbose方式，输出测试信息
    unittest.main()
