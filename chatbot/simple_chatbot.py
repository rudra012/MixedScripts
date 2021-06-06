# https://www.simplifiedpython.net/python-chatbot/
# pip install chatterbot==1.0.5 chatterbot_corpus==1.2.0
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('MyChatBot')
bot.set_trainer(ListTrainer)

conversation = open('chats.txt', 'r').readlines()

bot.train(conversation)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
    print('ChatBot:', reply)
    if message.strip() == 'Bye':
        print('ChatBot:Bye')
        break
