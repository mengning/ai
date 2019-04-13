import tts_Player
import time
#这里需要申请讯飞API ，并进行防火墙配置
#每个免费账户有每天500次限制
#可以在列表里输入多个账号，每次播放均会自动进行账户切换
ttsplayer = tts_Player.ttsPlayer(accountList = [{'APPID' : '5cad4c88','API_KEY' : "aa60ff625914e7029fa74465c4cd678d"}])

#这里有多种音色可供选择，通过speaker变量控制
ttsplayer.speaker = ttsplayer.XiaoYan


while True:
    text = input(">>>Please input the text,exit with 'exit'\n")
    if text == 'exit':
        break
    else:
        ttsplayer.ttsPlay(text)
