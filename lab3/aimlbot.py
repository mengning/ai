# -*- coding: utf-8 -*-
import aiml
import os
import record
import speach_recognize
import tts_Player
import time


mybot_path = '../lab1/mybot/'
# 切换到语料库所在工作目录
os.chdir(mybot_path)

mybot = aiml.Kernel()#创建一个aiml对象

mybot.learn("std-startup.xml")
#创建一个名为std-startup.xml的启动文件，作为加载AIML文件的主入口点。
mybot.respond('load aiml c')
#在std-srartup.xml文件里面可以创建更多的匹配模式以及加入更多的语料库。

#用语音输入代替文字输入
myrecorder = record.recorder(record_seconds=5)   # 录音对象，设定持续大约5秒
sr = speach_recognize.speachRecognizer(accountList = [{'APPID':'5cad4c88','API_KEY':'55dba8b5606fac7572450e79a2f03bcc'}])  # 输入科大讯飞统一平台的APPID 和 对应语音识别的API_KEY
#这里需要使用讯飞语音合成API
ttsplayer = tts_Player.ttsPlayer(accountList = [{'APPID' : '5cad4c88','API_KEY' : "aa60ff625914e7029fa74465c4cd678d"}])
#这里有多种音色可供选择，通过speaker变量控制
ttsplayer.speaker = ttsplayer.XiaoYan
print("小爱: 可以和我聊聊吗？")
while True:
    print(input("请说出您的问题？输入回车键开始录音~\n"))
    myrecorder.save_record()      # 开始录音
    sr.setAudiFile('audio.wav')   # 生成audio.wav录音文件
    question = sr.getResponse()   # 调用科大讯飞的API 识别audio.wav录音，转译成对应的文字
    if question.strip()=='':
            ttsplayer.ttsPlay("您说什么我没有听清楚！")
    else:
        print("你说的是："+question)
        response = mybot.respond(question[:-1])  # 聊天机器人进行回答
        print("小爱: ", response)               # 输出回答的问题
        ttsplayer.ttsPlay(response)