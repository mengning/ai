import requests
import time
import hashlib
import base64
import random
import threading
import simpleaudio as sa
from threading import Event


class ttsPlayer():
    XiaoXin = 'x_xiaoxin'
    ZhiLin = 'x_zhilin'
    XiaoWanZi = 'x_xiaowanzi'
    XiaoYan = 'xiaoyan'
    XiaoFang = 'x_xiaofang'
    def __init__(self,accountList = [{'APPID' : '5cad4c88','API_KEY' : "aa60ff625914e7029fa74465c4cd678d "}]):
        self.URL = "http://api.xfyun.cn/v1/service/v1/tts"
        self.AUE = "raw"
        self.speaker = self.XiaoFang
        self.accountList = accountList
        random.shuffle(self.accountList)
        self.accountIdx = 0
        self.APPID = self.accountList[self.accountIdx]['APPID']
        self.API_KEY = self.accountList[self.accountIdx]['API_KEY']

    def getHeader(self):
        curTime = str(int(time.time()))
        # ttp=ssml
        param = "{\"aue\":\"" + self.AUE + "\",\"auf\":\"audio/L16;rate=16000\",\"voice_name\":\""+self.speaker+"\",\"engine_type\":\"intp65\"}"
        #print("param:{}".format(param))

        paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
        #print("x_param:{}".format(paramBase64))

        m2 = hashlib.md5()
        m2.update((self.API_KEY + curTime + paramBase64).encode('utf-8'))

        checkSum = m2.hexdigest()
        #print('checkSum:{}'.format(checkSum))

        header = {
            'X-CurTime': curTime,
            'X-Param': paramBase64,
            'X-Appid': self.APPID,
            'X-CheckSum': checkSum,
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }
        #print(header)
        return header


    def getBody(self,text):
        data = {'text': text}
        return data

    def switchAccount(self):
        self.accountIdx = (self.accountIdx+1)%len(self.accountList)
        self.APPID = self.accountList[self.accountIdx]['APPID']
        self.API_KEY = self.accountList[self.accountIdx]['API_KEY']


    def getContent(self,text):
        content = b''
        r = requests.post(self.URL, headers=self.getHeader(), data=self.getBody(text))
        contentType = r.headers['Content-Type']
        #print('header',r.headers)
        #print('content',r.content)
        #print(self.APPID,'===',self.API_KEY)
        if contentType == "audio/mpeg":
            self.switchAccount()
            sid = r.headers['sid']
            if self.AUE == "raw":
                return r.content
        else:
            contentDict = eval(bytes.decode(r.content))
            if (contentDict['desc'] == 'illegal parameter|illegal text length'):
                sequences = str.split(text,'。')
                sequences = [word for word in sequences if word!='']
                text1 = '。'.join(sequences[:int(len(sequences)/2)])
                text2 = '。'.join(sequences[int(len(sequences)/2):])
                if(text1==''):
                    text1 = text[:len(text)/2]
                    text2 = text[len(text)/2:]
                try:
                    content += self.getContent(text1)
                except:
                    print('error：when print ',text1)
                try:
                    content += self.getContent(text2)
                except:
                    print('error: when print ',text2)
                print(r.content)
                return content

    class myThread(threading.Thread):
        def __init__(self, threadID, content,event = Event()):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.content = content
            self.event = event
        def run(self):
            #print("开始线程：" + self.name)
            sa.play_buffer(self.content, 1, 2, 16000)
            #print('sleep_time',len(self.content) / 32000)
            time.sleep(len(self.content)/32000)
            #print("退出线程：" + self.name)
            self.event.set()

    def ttsPlay(self,text,event = Event()):
        content = self.getContent(text)
        time.sleep(0.3)
        # print('content',content)
        if(content!=''):
            playaudiothread = self.myThread('playaudio',content,event=event)
            playaudiothread.start()
            event.wait()
            #print('complete!')
            self.switchAccount()

