import telebot
import requests
import json
import datetime
token='5252576667:AAFQqRljsSchLpI7Lb0od_33xT5w2kMpiF8'
bot = telebot.TeleBot(token=token)
covid_api = 'https://covid-api.mmediagroup.fr/v1/cases?country={country}'

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, "Hello, I am Covid19-Bot Tell me Country: ")

@bot.message_handler(content_types='text')
def send_data(message):
    covid = requests.get(covid_api.format(country=message.text.title()))
    covid_json = covid.json()
    con = covid_json['All']['confirmed']
    de = covid_json['All']['deaths']
    re = covid_json['All']['recovered']
    co = covid_json['All']['country']
    po = covid_json['All']['population']
    bot.send_message(message.chat.id, f'🤒 Confirmed { con }')
    bot.send_message(message.chat.id, f'💀 Dead { de }')
    bot.send_message(message.chat.id, f'😷 Recovered { re }')
    bot.send_message(message.chat.id, f'Country :{ co }')
    bot.send_message(message.chat.id,f'Population : { po }')
    today = datetime.datetime.now()
    data = f'All Count covid incidence. {message.text.title()}: {covid_json["All"]["confirmed"]} Today date: {today.day}-{today.month}-{today.year}'
    bot.send_message(message.chat.id, data)

print('Bot is working.....')
bot.infinity_polling()

# @Cpvid19kg_bot