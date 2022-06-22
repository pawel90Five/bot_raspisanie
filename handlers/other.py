from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_other
from data_base import sqlite_db


# dp.message_handler(commands=['start', 'help'])
async def start_bot(message: types.Message):
    await message.reply('Бот для Авиционного Технического Колледжа города Кумертау.\n\
        /сегодня - узнать расписание на сегодня\n\
        /завтра - узнать расписание на завтра\n',
        parse_mode="HTML", disable_web_page_preview=True, reply_markup=kb_other)


async def sender(message: types.Message, when: int):
    groups = message.get_args()
    if len(groups):
        await message.reply(await sqlite_db.getGroup_schedule(when, *groups.split()), parse_mode='HTML')
    else:
        await message.reply(await sqlite_db.getAll_schedule(when), parse_mode='HTML')


# dp.message_handler(commands=['сегодня'])
async def today_send(message: types.Message):
    await sender(message, -1)


# dp.message_handler(commands=['завтра'])
async def tomorrow_send(message: types.Message):
    await sender(message, 1)


# @dp.message_handler(commands=['саня'])
async def sanya_send(message: types.Message):
    await message.answer(message.text + ' молодца @Posssshlyak')


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start', 'help'])
    dp.register_message_handler(today_send, commands=['сегодня'])
    dp.register_message_handler(tomorrow_send, commands=['завтра'])
    dp.register_message_handler(sanya_send, commands=['саня'])
    # dp.register_message_handler(echo_send)
