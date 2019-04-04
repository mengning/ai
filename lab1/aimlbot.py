# -*- coding: utf-8 -*-
import aiml
import os


mybot_path = './mybot'
# 切换到语料库所在工作目录
os.chdir(mybot_path)

mybot = aiml.Kernel()#创建一个aiml对象

mybot.learn("std-startup.xml")
#创建一个名为std-startup.xml的启动文件，作为加载AIML文件的主入口点。
mybot.respond('load aiml c')
#在std-srartup.xml文件里面可以创建更多的匹配模式以及加入更多的语料库。

while True:
        print (mybot.respond(input("Enter your Message>> ")))
