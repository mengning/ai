#-*- coding: utf-8 -*-
#!/usr/bin/env python3

import pyaudio
import wave
import time
import threading
class recordor():
    
    def __init__(self,chunk=1024, channel=1, rate=8000, record_seconds=10):
        self.CHUNK = chunk
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = channel
        self.RATE = rate
        self.RECORD_SECONDS = record_seconds
        self.run = True
        self.name = "audio.wav"
        
    def record(self):
        self.p = pyaudio.PyAudio()
    
        stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
    
        print("* recording")
        self.frames = []     
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):           
            if(self.run):
                data = stream.read(self.CHUNK)
                self.frames.append(data)
            else:
                break
        
        print('* saving recording...')
        stream.stop_stream()
        stream.close()
        self.p.terminate()
              
    def setRunFlag(self,flag):
        if(flag == "stop"):
            self.run = False
                    
    def save_record(self):
        self.record()
        wf = wave.open(self.name, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print("record complete")
   
if __name__ == '__main__':   
    myrecorder = recordor()
    myrecorder.save_record()
    
    
