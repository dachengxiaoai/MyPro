#coding:utf-8

import unittest
from time import sleep
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class LoveHostTest(unittest.TestCase): #使用unittest
    def setUp(self):
        url = "https://passport.5i5j.com/passport/login?service=https%3A%2F%2Fbj.5i5j.com%2Freglogin%2Findex%3FpreUrl%3Dhttps%253A%252F%252Fbj.5i5j.com%252F%253Fpmf_group%253Dbaidu%2526pmf_medium%253Dppzq%2526pmf_plan%253D%2525E5%2525B7%2525A6%2525E4%2525BE%2525A7%2525E6%2525A0%252587%2525E9%2525A2%252598%2526pmf_unit%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526pmf_keyword%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526pmf_account%253D160&status=1&city=bj"
        self.chrome = webdriver.Chrome()
        self.chrome.get(url)

    def login(self,username,password):
        user = self.chrome.find_element_by_id("username")
        password = self.chrome.find_element_by_id("password")
        submit = self.chrome.find_element_by_id("login")

        user.send_keys(username)
        password.send_keys(password)
        submit.click()
    def test_login(self):
        self.login("13331153360","123123")
        sleep(3)
        errormessage = "用户名或密码错误"
        loginText = self.chrome.find_element_by_id("erromsg")
        self.assertEquals(errormessage,loginText)

    def tearDown(self):
        sleep(10)
        self.chrome.close()

if __name__ == "__main__":
    sut = unittest.TestSuite()
    sut.addTest(LoveHostTest("test_login"))

    with open("love.html","wb") as f:
        runner = HTMLTestRunner(
            stream = f,
            title = "loveTest",
            description = "this is our Test"
        )
        runner.run(sut)



