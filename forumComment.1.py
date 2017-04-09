#-*-coding:utf-8-*-
from selenium import webdriver
import time
import random, sqlite3

"""
auto login in baiduyunbbs site, and comment postings on the site for earn froum Gold

timestamp: 2017-03-11
author: yuippe
"""

##最新主题对应的id
newestSubjectList = [
    "//li[@class='dx-icon-0']/em/a[2]",
    "//li[@class='dx-icon-1']/em/a[2]",
    "//li[@class='dx-icon-2']/em/a[2]",
    "//li[@class='dx-icon-3']/em/a[2]",
    "//li[@class='dx-icon-4']/em/a[2]",
    "//li[@class='dx-icon-5']/em/a[2]",
    "//li[@class='dx-icon-6']/em/a[2]",
    "//li[@class='dx-icon-7']/em/a[2]"
]

##site
loginurl = 'http://www.baiduyunbbs.com/'
browser = webdriver.Chrome()
browser.get(loginurl)

browser.find_element_by_xpath("//ul[@id='dx-threads-hd']/li[1]/span").click()
subjectStr1 = browser.find_element_by_xpath("//div[@id='dx-threads-0']/ul[@class='dx-list']/li[1]/em/a[2]").text
subjectStr2 = browser.find_element_by_xpath("//div[@id='dx-threads-0']/ul[@class='dx-list']/li[2]/em/a[2]").text
subjectStr3 = browser.find_element_by_xpath("//div[@id='dx-threads-0']/ul[@class='dx-list']/li[3]/em/a[2]").text
subjectStr4 = browser.find_element_by_xpath("//div[@id='dx-threads-0']/ul[@class='dx-list']/li[4]/em/a[2]").text
subjectStr5 = browser.find_element_by_xpath("//div[@id='dx-threads-0']/ul[@class='dx-list']/li[5]/em/a[2]").text
subjectStr6 = browser.find_element_by_xpath("//div[@id='dx-threads-0']/ul[@class='dx-list']/li[6]/em/a[2]").text
subjectStr7 = browser.find_element_by_xpath("//div[@id='dx-threads-0']/ul[@class='dx-list']/li[7]/em/a[2]").text
subjectStr8 = browser.find_element_by_xpath("//div[@id='dx-threads-0']/ul[@class='dx-list']/li[8]/em/a[2]").text



print subjectStr1
print subjectStr2
print subjectStr3
print subjectStr4
print subjectStr5
print subjectStr6
print subjectStr7
print subjectStr8








