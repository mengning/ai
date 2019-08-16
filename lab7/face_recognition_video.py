import cv2
import face_recognition
import numpy as np
import os
import aiml
import os
import record
import speach_recognize
import tts_Player
import time
import awake_recognize


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
monitor_flag = False

known_face_dir = 'known_images'
video_capture = cv2.VideoCapture(0)

known_file_list = os.listdir(known_face_dir)
known_face_names = []
known_face_encodings = []
resize_fx = 0.5
resize_fy = 0.5

for known_img_file in known_file_list:
    if known_img_file.endswith('.jpg'):
        img = face_recognition.load_image_file(os.path.join(known_face_dir,known_img_file))
        encoding = face_recognition.face_encodings(img)[0]
        name = known_img_file[:-4]
        known_face_names.append(name)
        known_face_encodings.append(encoding)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
name_remember  = []
name_counter = 0

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=resize_fx, fy=resize_fy)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.35)
            name = "Unknown"
            # # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                 first_match_index = matches.index(True)
                 name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= int(1/resize_fy)
        right *= int(1/resize_fx)
        bottom *= int(1/resize_fy)
        left *= int(1/resize_fx)

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom ), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom + 29), font, 1.0, (255, 255, 255), 1)
        if name != name_remember and name != "Unknown":
            name_remember  = name
            name_counter = 0
        if name == name_remember:
            name_counter = name_counter + 1
            if name_counter >= 20:
                name_counter = 0
                ttsplayer.ttsPlay("您好，"+ name)
                monitor_flag = True

    # Display the resulting image
    cv2.imshow('Video', frame)
    if monitor_flag:
        monitor_flag = False
        ttsplayer.ttsPlay("有什么可以帮您？")
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
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()