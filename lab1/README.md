# 搭建智能对话系统

* 使用[ChatterBot](https://github.com/gunthercox/ChatterBot)搭建闲聊对话系统
```
pip3 install chatterbot
pip3 install chatterbot-corpus
git clone https://github.com/mengning/ai.git
cd ai/lab1
ai/lab1$ python chatterbot.py
# 删除生成的临时问题
rm db.sqlite3* __pycache__/ sentence_tokenizer.pickle  -rf
```
* 使用AIML搭建特定功能的对话系统
```
pip3 install aiml
git clone https://github.com/mengning/ai.git
cd ai/lab1
ai/lab1$ python aimlbot.py
```
