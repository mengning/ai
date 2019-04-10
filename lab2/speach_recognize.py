#-*- coding: utf-8 -*-
#!/usr/bin/env python3

import time
import json
import hashlib
import base64
import requests
import random
class speachRecognizer():
    def __init__(self,aue="raw",engineType = "sms8k",accountList = []):
        self.aue = aue
        self.engineType = engineType
        self.URL = "http://api.xfyun.cn/v1/service/v1/iat"
        self.APPID = ""
        self.API_KEY = ""
        self.appidPool = accountList
        self.loopAPPKEY()

    def getHeader(self):
        curTime = str(int(time.time()))
        # curTime = '1526542623'
        param = "{\"aue\":\"" + self.aue + "\"" + ",\"engine_type\":\"" + self.engineType + "\"}"
        # print("param:{}".format(param))
        paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
        # print("x_param:{}".format(paramBase64))
    
        m2 = hashlib.md5()
        m2.update((self.API_KEY + curTime + paramBase64).encode('utf-8'))
        checkSum = m2.hexdigest()
        # print('checkSum:{}'.format(checkSum))
        header = {
            'X-CurTime': curTime,
            'X-Param': paramBase64,
            'X-Appid': self.APPID,
            'X-CheckSum': checkSum,
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }
        # print(header)
        return header
    
    def getbody(self, filePath):
        binFile = open(filePath, 'rb')
        data = {'audio': base64.b64encode(binFile.read())}
        # print(data)
        # print('data:{}'.format(type(data['audio'])))
        # print("type(data['audio']):{}".format(type(data['audio'])))
        return data
    
    def setAudiFile(self, audioName):
        self.filePath = audioName
    
    def loopAPPKEY(self):
        id = random.randrange(0,len(self.appidPool))
        self.APPID = self.appidPool[id]['APPID']
        self.API_KEY = self.appidPool[id]['API_KEY']
    
    def getResponse(self):       
        responseInfo = requests.post(self.URL, headers=self.getHeader(), data=self.getbody(self.filePath))
        dictResponse = eval(responseInfo.content.decode('utf-8'))
        if dictResponse["desc"] == "success":
            self.loopAPPKEY()
            return dictResponse["data"]
        else:
            return dictResponse["desc"]

if __name__ == '__main__':
    mySR = speachRecognizer()
    mySR.setAudiFile('2018-12-29.wav')
    print(mySR.getResponse())