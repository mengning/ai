import pyaudio
import numpy as np
import time
import os
import aiml
import record
import speach_recognize
import tts_Player
import jieba
from threading import Event

def Monitor(threshold = 1000):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 8000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = 'monitor_tmp.wav'
    THRESHOLD = threshold

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = CHUNK
                    )
    frames = []
    while True:
        for i in range(3):
            data = stream.read(CHUNK)
            frames.append(data)
        audio_data = np.fromstring(data,dtype=np.short)
        large_sample_count = np.sum(audio_data>THRESHOLD)
        temp = np.max(audio_data)
        if temp > THRESHOLD:
            time.sleep(1)
            break
    stream.stop_stream()
    stream.close()
    p.terminate()
    return True

if __name__ == '__main__':
    while True:
        print("大声说“嗨”可以唤醒我哦~\n")
        monitor_flag = False
        while not monitor_flag:
            monitor_flag = Monitor(threshold = 500)
        print("嗯哼！我再睡会~\n")

