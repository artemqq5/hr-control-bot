from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup


class BackEmployeesNavigation(CallbackData, prefix="BackEmployeesNavigation"):
    pass


kb_back_employees_nav = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackEmployeesNavigation().pack())]
])
