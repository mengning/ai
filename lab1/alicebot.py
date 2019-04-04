# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("小爱")

# 列表方式的对话学习
conversation = [
    "你是谁？",
    "我是小爱呀！"
]
trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
# 文件方式的对话学习
trainer.train(
    "./mybot/conversations.yml"
)
# chatterbot.corpus语料库学习
# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")
# Train the chatbot based on the chinese corpus
trainer.train("chatterbot.corpus.chinese")


while True:
        # Get a response to an input statement
        response = chatbot.get_response(input("YOU: "))      
        print("小爱: ", response)
        