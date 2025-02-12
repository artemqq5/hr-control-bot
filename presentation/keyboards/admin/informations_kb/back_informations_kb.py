from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup


class BackInformationsNavigation(CallbackData, prefix="BackInformationsNavigation"):
    pass


kb_back_informations_nav = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.GENERAL.BACK(), callback_data=BackInformationsNavigation().pack())]
])
