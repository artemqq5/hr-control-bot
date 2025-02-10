from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.access_kb.back_access_kb import BackUsersNavigation


class AddEmployee(CallbackData, prefix="AddEmployee"):
    pass


