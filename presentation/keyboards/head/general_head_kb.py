from aiogram_i18n import L
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu_head = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.GENERAL.INFORMATION.CREATE())],
    [KeyboardButton(text=L.HEAD.INFORMATIONS())],
], resize_keyboard=True)
