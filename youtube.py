from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
import logging
import download
import os
import validation

logging.basicConfig(level=logging.INFO)
bot = Client("ses1", workers=5, api_id=21235718, api_hash='d521c7a63d9c6b2a2ae284b8441e29a1',
             bot_token='5605615812:AAELTBtEgveNbGj80XrQjSsLB8fQi9mrZbQ')


@bot.on_message(filters.command("start", ["!", "/"]))
def connect(chat, m):
    try:
        user_id = m.chat.id
        bot.send_message(user_id,
                         'Привет! Я умею скачивать видео из YouTube. Отправь мне ссылку — а я отправлю тебе скачанное видео')
    except Exception as e:
        print(e)


@bot.on_message(filters.text)
def get(chat, m):
    url = m.text
    user_id = m.chat.id
    try:
        VID_ID = ''
        VID_ID = validation.to_valid(url, VID_ID)
        bot.send_message(m.chat.id, 'Начинаем загрузку видео...')
        download.worker(VID_ID)
        bot.send_video(m.chat.id, str(VID_ID) + '.mp4')
        os.remove(VID_ID + '.mp4')
    except Exception as e:
        bot.send_message(m.chat.id, f'Что-то пошло не так! Ошибка `{e}`')


bot.run()
