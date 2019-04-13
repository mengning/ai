# 语音合成和语音播放

* 安装和使用simpleaudio
```
pip3 install simpleaudio
```
使用simpleaudio播放音频数据
```
import simpleaudio as sa
sa.play_buffer(self.content, 1, 2, 16000)
```

* 使用科大讯飞的在线语音合成API

Requests is an elegant and simple HTTP library for Python
```
pip3 install requests
```

科大讯飞语音合成接口将文字信息转化为声音信息，同时提供了众多极具特色的发音人（音库）供选择。
```
POST http[s]://api.xfyun.cn/v1/service/v1/tts HTTP/1.1
Content-Type:application/x-www-form-urlencoded; charset=utf-8
```
借助requests HTTP库可以将将音频一次性发送至云端，块式传输。

* 语音合成演示范例
```
python example_tts.py
```
## Refers

* https://doc.xfyun.cn/rest_api/语音合成.html
