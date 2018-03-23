import telebot
import os
import random
import urllib.request as urllib2

token="543828801:AAGVBMsl1jBbJKYUKYK_F00Kf0sBYkgamsI"
bot=telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def statr(message):
    bot.send_message(message.from_user.id, 'Добро пожаловать')

bot.polling(none_stop=True)