#coding:utf-8
from time import sleep
from selenium import webdriver

#创建了浏览器驱动实例
chrome = webdriver.Chrome()

#访问指定网页
chrome.get("https://www.baidu.com/")

#通过HTML id查找input框
keys = chrome.find_element_by_id("kw")

#在input当中添加值
keys.send_keys("python")

#挂起6秒
sleep(6)

#退出浏览器
chrome.close()