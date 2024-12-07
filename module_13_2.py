from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
#создаем хендлер, отвечающий на запрос команды /start
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
#создаем общий хендлер, отвечающий на любой запрос, кроме ввода команды start
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__== '__main__':
    executor.start_polling(dp,skip_updates=True)
