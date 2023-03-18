from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio
import requests
import os

BASE_URL = 'https://api.telegram.org/bot'
TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_message(msg: types.Message):
    await msg.reply('Я - эхо-бот!')


@dp.message_handler(commands='help')
async def help_message(msg: types.Message):
    await msg.reply('Я повторю твое сообщение!')


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)


# BASE_URL = 'https://api.telegram.org/bot'
# TOKEN = os.environ['TOKEN']


# def get_updates():
#     r = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
#     message = r['result'][-1]['message']
#     user = message['from']['id']
#     if 'text' in message:
#         txt = message['text']
#         requests.get(
#             f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user}&text={txt}')
#     if 'photo' in message:
#         photo = message['photo'][-1]['file_id']
#         if 'caption' in message:
#             cap = message['caption']
#             requests.get(
#                 f'{BASE_URL}{TOKEN}/sendPhoto?chat_id={user}&photo={photo}&caption={cap}')
#         else:
#             requests.get(
#                 f'{BASE_URL}{TOKEN}/sendPhoto?chat_id={user}&photo={photo}')
#     if 'audio' in message:
#         audio = message['audio']['file_id']
#         if 'caption' in message:
#             cap = message['caption']
#             requests.get(
#                 f'{BASE_URL}{TOKEN}/sendAudio?chat_id={user}&audio={audio}&caption={cap}')
#         else:
#             requests.get(
#                 f'{BASE_URL}{TOKEN}/sendAudio?chat_id={user}&audio={audio}')
#     if 'document' in message:
#         doc = message['document']['file_id']
#         if 'caption' in message:
#             cap = message['caption']
#             requests.get(
#                 f'{BASE_URL}{TOKEN}/sendDocument?chat_id={user}&document={doc}&caption={cap}')
#         else:
#             requests.get(
#                 f'{BASE_URL}{TOKEN}/sendDocument?chat_id={user}&document={doc}')
#     if 'sticker' in message:
#         sticker = message['sticker']['file_id']
#         requests.get(
#             f'{BASE_URL}{TOKEN}/sendSticker?chat_id={user}&sticker={sticker}')
#     if 'video' in message:
#         video = message['video']['file_id']
#         if 'caption' in message:
#             cap = message['caption']
#             requests.get(
#                 f'{BASE_URL}{TOKEN}/sendVideo?chat_id={user}&video={video}&caption={cap}')
#         else:
#             requests.get(
#                 f'{BASE_URL}{TOKEN}/sendVideo?chat_id={user}&video={video}')
#     if 'voice' in message:
#         voice = message['voice']['file_id']
#         requests.get(
#             f'{BASE_URL}{TOKEN}/sendVoice?chat_id={user}&voice={voice}')
#     if 'contact' in message:
#         contact = message['contact']
#         number = contact['phone_number']
#         name = contact['first_name']
#         requests.get(
#             f'{BASE_URL}{TOKEN}/sendContact?chat_id={user}&phone_number={number}&first_name={name}')
#     if 'location' in message:
#         loc = message['location']
#         lat = loc['latitude']
#         lon = loc['longitude']
#         requests.get(
#             f'{BASE_URL}{TOKEN}/sendLocation?chat_id={user}&latitude={lat}&longitude={lon}')


# get_updates()

