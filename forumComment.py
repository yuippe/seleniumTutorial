#-*-coding:utf-8-*-
from selenium import webdriver
import time
import random, sqlite3

"""
auto login in baiduyunbbs site, and comment postings on the site for earn froum Gold

timestamp: 2017-03-11
author: yuippe
"""

exec_num=1;

##最新主题对应的id
newestSubjectList = [
    "//div[@id='dx-threads-0']/ul[@class='dx-list']/li[1]/em/a[2]",
    "//div[@id='dx-threads-0']/ul[@class='dx-list']/li[2]/em/a[2]",
    "//div[@id='dx-threads-0']/ul[@class='dx-list']/li[3]/em/a[2]",
    "//div[@id='dx-threads-0']/ul[@class='dx-list']/li[4]/em/a[2]",
    "//div[@id='dx-threads-0']/ul[@class='dx-list']/li[5]/em/a[2]",
    "//div[@id='dx-threads-0']/ul[@class='dx-list']/li[6]/em/a[2]",
    "//div[@id='dx-threads-0']/ul[@class='dx-list']/li[7]/em/a[2]",
    "//div[@id='dx-threads-0']/ul[@class='dx-list']/li[8]/em/a[2]"
]

##comments sets
commentsSentenceList = [
    u"还不错,先下载看看",u"感谢分享，下载看看",u"更新速度很快快，赞",u"论坛真是给力",
    u"好资源，不回帖就太对不起楼主了",u"谢谢分享，够快！",u"这年头这种好人不多了，加油！",u"还不错,先下载看看",
    u"非常好的资源，谢谢分享",u"速度下载，太感谢了，感恩百度云论坛无私的分享与奉献 "
]

alreadyCommsList = []

commsLen = len(commentsSentenceList)

##site
loginurl = 'http://www.baiduyunbbs.com/'

browser = webdriver.Chrome()
browser.get(loginurl)

##login in
browser.find_element_by_id('ls_username').clear()
browser.find_element_by_id('ls_username').send_keys(u"绿韵飞阳")
browser.find_element_by_id('ls_password').clear() 
browser.find_element_by_id('ls_password').send_keys("lvzhiyun")
browser.find_element_by_xpath("//button").click()
time.sleep(3)

##if not existed, then create, or open db
cx = sqlite3.connect("E:/workspace/seleniumDemo/forumComment.db")
cu = cx.cursor()

##start comments
def startComments(driverInstance, login_url):
    for newcomm in newestSubjectList:
        driverInstance.get(login_url)
        driverInstance.find_element_by_xpath("//ul[@id='dx-threads-hd']/li[1]/span").click()
        subjectStr = driverInstance.find_element_by_xpath(newcomm).text
        print subjectStr
        cu.execute("select * from postsalreadycomms where subjecttest=?",(subjectStr,))
        if len(cu.fetchall()) == 0:
            ##表示该帖子没有被评论
            driverInstance.find_element_by_xpath(newcomm).click()
            driverInstance.find_element_by_id("fastpostmessage").clear()
            
            randNum = random.randint(1,1000)
            luckNum = randNum % commsLen
            luckCommsStr = commentsSentenceList[luckNum]

            driverInstance.find_element_by_id("fastpostmessage").send_keys(luckCommsStr)
            driverInstance.find_element_by_xpath("//button[@id='fastpostsubmit']/strong").click()
            cu.execute("insert into postsalreadycomms(subjecttest) values (?)", (subjectStr,))
            cx.commit()
            time.sleep(50)
        else:
            continue
    

##interval time to exec
def run(interval,browser_1,loginurl_1,func_toexe):
    while True:
        try:
            global exec_num
            time_remaining = interval-time.time()%interval
            time.sleep(time_remaining)
            func_toexe(browser_1,loginurl_1)
            exec_num=exec_num+1
            print exec_num
        except Exception, e:
            print e


if __name__ == '__main__':
    interval = 180;
    #f = startComments(browser,loginurl)
    run(interval,browser,loginurl,startComments)







