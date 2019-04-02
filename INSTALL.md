# 环境安装配置

* 安装python3和pip。您从https://www.python.org/downloads/ 下载对应的安装包安装，Ubuntu Linux下可以使用如下命令安装查看python3和pip。
```
sudo apt install python3
python3 -v 
pip --version # Python 2.7.9 + 或 Python 3.4+ 以上版本都自带 pip 工具
pip install -U pip # 如果这个升级命令出现问题 ，可以使用以下命令：sudo easy_install --upgrade pip
```
* 安装其他相关工具和库
```
pip install ggplot # python的常用可视化包：Matplotlib，基于该包的二次开发的包（Pandas，Seaborn，ggplot） 动态图的绘制：Plotly，pyecharts（可在网页中展示动态图），是否必须？
pip install PyAudio
```
