# 环境安装配置

* 安装python3和pip。您从https://www.python.org/downloads/ 下载对应的安装包安装，Ubuntu Linux下可以使用如下命令安装查看python3和pip3。
```
sudo apt install python3
sudo apt install python3-pip

python3 -v 
pip3 --version
```

在Windows下安装好python3后需要设置环境变量，右击“我的电脑”->属性->高级系统设置->环境变量，然后将YOUR-INSTALL-PATH\Python\Python36和YOUR-INSTALL-PATH\Python\Python36\Scripts 添加到Path里，这样就可以在cmd命令行下使用python和pip命令了。

* 安装git，您可以从https://desktop.github.com/ 下载github的桌面安装包，Ubuntu Linux下可以使用如下命令安装
```
sudo apt install git
```

# 人脸识别环境安装配置

```
pip install cmake
pip install dlib
```
