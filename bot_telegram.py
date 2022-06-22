from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db

from handlers import other


async def on_startup(_):
    print('Бот ожил')
    sqlite_db.sql_start()


other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
