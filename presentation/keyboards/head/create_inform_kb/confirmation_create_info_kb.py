from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class ConfirmationCreateInform(CallbackData, prefix="ConfirmationCreateInform"):
    pass


kb_confirmation_create_inform = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.GENERAL.CONFIRMATION(), callback_data=ConfirmationCreateInform().pack())],
])
