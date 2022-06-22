from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/сегодня')
b2 = KeyboardButton('/завтра')


kb_other = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_other.row(b1, b2)
