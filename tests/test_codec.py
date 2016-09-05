# coding: utf-8

import unittest
from pcfg import codec

class TestCodec(unittest.TestCase):
    def setUp(self):
        self.number = 1653522623
        self.code = b'b\x8e\xc0\xbf'

    def tearDown(self):
        pass

    def test_encode(self):
        code = codec.encode(self.number)
        self.assertEqual(code, self.code)

    def test_decode(self):
        number = codec.decode(self.code)
        self.assertEqual(number, self.number)


if __name__ == '__main__':
    # __import__("sys").argv.append("-v")         # 采用verbose方式，输出测试信息
    unittest.main()
