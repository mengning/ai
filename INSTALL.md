# 环境安装配置

* 安装python3和pip。您从https://www.python.org/downloads/ 下载对应的安装包安装，Ubuntu Linux下可以使用如下命令安装查看python3和pip3。
```
sudo apt install python3
sudo apt install python3-pip
python3 -v 
pip3 --version # Python 2.7.9 + 或 Python 3.4+ 以上版本都自带 pip 工具
```

在Windows下安装好python3后需要设置环境变量，右击“我的电脑”->属性->高级系统设置->环境变量，然后将YOUR-INSTALL-PATH\Python\Python36和YOUR-INSTALL-PATH\Python\Python36\Scripts 添加到Path里，这样就可以在cmd命令行下使用python和pip命令了。

* 安装其他相关工具和库
```
pip3 install ggplot # python的常用可视化包：Matplotlib，基于该包的二次开发的包（Pandas，Seaborn，ggplot） 动态图的绘制：Plotly，pyecharts（可在网页中展示动态图），是否必须？Ubuntu18.04和Windows下都安装失败，好像是超时，有没有替代的安装源？
pip3 install PyAudio # Ubuntu18.04下安装失败
```

# lab1

* 使用[ChatterBot](https://github.com/gunthercox/ChatterBot)搭建闲聊对话系统
```
pip3 install chatterbot
pip3 install chatterbot-corpus
git clone https://github.com/mengning/ai.git
cd ai/lab1
ai/lab1$ python chatterbot.py
```
* 使用AIML搭建特定功能的对话系统
```
pip3 install aiml
git clone https://github.com/mengning/ai.git
cd ai/lab1
ai/lab1$ python aimlbot.py
```
