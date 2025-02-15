from aiogram_i18n import L
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu_admin = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.ADMIN.INFORMATIONS())],
    [KeyboardButton(text=L.ADMIN.HEADS_ACCESS())],
    [KeyboardButton(text=L.ADMIN.EMPLOYEES())],
    [KeyboardButton(text=L.GENERAL.INFORMATION.CREATE())],
], resize_keyboard=True)
