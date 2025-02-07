from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup


class BackUsersNavigation(CallbackData, prefix="BackUsersNavigation"):
    pass


kb_back_users_nav = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackUsersNavigation().pack())]
])
