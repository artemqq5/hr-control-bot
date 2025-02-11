from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.access_kb.back_access_kb import BackUsersNavigation


class GenerateAccess(CallbackData, prefix="GenerateAccess"):
    pass


class ConfirmationGenerateAccess(CallbackData, prefix="ConfirmationGenerateAccess"):
    pass


kb_confirmation_generate_access = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.GENERAL.CONFIRMATION(), callback_data=ConfirmationGenerateAccess().pack())],
    [InlineKeyboardButton(text=L.GENERAL.BACK(), callback_data=BackUsersNavigation().pack())]
])
