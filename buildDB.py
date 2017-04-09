#-*-coding:utf-8-*-
from selenium import webdriver
import time
import random, sqlite3


cx = sqlite3.connect("E:/workspace/seleniumDemo/forumComment.db")

cu = cx.cursor()
##cu.execute("CREATE TABLE postsalreadycomms1 (ID INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1, subjecttest TEXT (100) UNIQUE, updatetime DATETIME DEFAULT (datetime('now', 'localtime')));")

subjectStr = u"中国"
cu.execute("select * from postsalreadycomms where subjecttest=?",(subjectStr,))
# for item in cu.fetchall():
#     print item

print len(cu.fetchall())