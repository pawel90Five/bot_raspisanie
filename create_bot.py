from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os


storage = MemoryStorage()

# bot = Bot(token=os.getenv('TOKEN'))
bot = Bot('5432736912:AAEBPU33wrccSUye8LHR5_sn-Y3XUVYvKxc')
dp = Dispatcher(bot, storage=storage)
