# 环境安装配置

* 安装python3和pip。您从https://www.python.org/downloads/ 下载对应的安装包安装，Ubuntu Linux下可以使用如下命令安装查看python3和pip3。
```
sudo apt install python3
sudo apt install python3-pip

python3 -v 
pip3 --version
```

在Windows下安装好python3后需要设置环境变量，右击“我的电脑”->属性->高级系统设置->环境变量，然后将YOUR-INSTALL-PATH\Python\Python36和YOUR-INSTALL-PATH\Python\Python36\Scripts 添加到Path里，这样就可以在cmd命令行下使用python和pip命令了。

* 安装vscode和git

Visual Studio Code（以下简称vscode）是一个轻量且强大的代码编辑器，支持Windows，OS X和Linux。内置JavaScript、TypeScript和Node.js支持，而且拥有丰富的插件生态系统，可通过安装插件来支持C++、C#、Python、PHP等其他语言。下载地址：https://code.visualstudio.com/#alt-downloads


您可以从https://desktop.github.com/ 下载github的桌面安装包，Ubuntu Linux下可以使用如下命令安装
```
sudo apt install git
sudo apt install ./<file>.deb #安装vscode的安装包
```
# 对话引擎

```
pip install chatterbot
pip install chatterbot-corpus
pip install aiml
```

# 智能语音

```
pip install PyAudio
pip install requests
pip install simpleaudio
```

# 人脸识别

```
pip install cmake
pip install dlib
pip install face_recognition
pip install opencv-python
```
