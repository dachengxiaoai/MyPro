#coding:utf-8

import unittest

class OurTest(unittest.TestCase):
    def setUp(self):
        """
        是TestCase定义好的，在测试开始前自动执行的方法
        所以我们经常在setUp当中准备测试的参数
        """
        self.arg1 = 1
        self.arg2 = 2
    def test_Something(self):
        """
        具体的测试功能，unittest当中所有的测试功能必须以test开头
        """
        self.assertEquals(self.arg1,self.arg2) #断言相等，是unittest封装好的方法
    def tearDown(self):
        """
        用于回收环境
        :return:
        """
        print("test over")

if __name__ == "__main__":
    unittest.main()