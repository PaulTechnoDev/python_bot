import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import api

users = ['suluguni_official', "roman_sysoev", 'ibaka222', 'restoratorgame', 'zbyka13', 'lilit9n', 'olyashaa',
         'igrog077', 'dokkorki']

params = {
    'user_login': users
}
ggUsers = 'lilit9n,gantver1'

load_dotenv()
bot = Bot(os.getenv('API'))
dp = Dispatcher(bot)

@dp.message_handler(commands='stream')
async def start(message: types.Message):
    await message.reply('\n'.join(api.getTwitchusers(params) + api.getGGusers(ggUsers)), disable_web_page_preview=True)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
