# 语音录制与语音识别

* 安装和使用PyAudio
```
pip install PyAudio
```
使用PyAudio采集声音数据，这里需要增加音频方面的基础知识以及PyAudio API的介绍
```
import pyaudio
p = pyaudio.PyAudio()
stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
data = stream.read(self.CHUNK)
frames.append(data)
stream.stop_stream()
stream.close()
p.terminate()
```
使用wave保持声音
```
import wave
wf = wave.open(self.name, 'wb')
wf.setnchannels(self.CHANNELS)
wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
wf.setframerate(self.RATE)
wf.writeframes(b''.join(self.frames))
wf.close()
```
* 使用科大讯飞的在线语音识别API

Requests is an elegant and simple HTTP library for Python
```
pip3 install requests
```

科大讯飞语音听写接口可将语音(≤60秒)转换成对应的文字信息。
```
POST http[s]://api.xfyun.cn/v1/service/v1/iat HTTP/1.1
Content-Type:application/x-www-form-urlencoded; charset=utf-8
```
借助requests HTTP库可以将将音频一次性发送至云端，块式传输。
## Refers

* https://doc.xfyun.cn/rest_api/语音听写.html
