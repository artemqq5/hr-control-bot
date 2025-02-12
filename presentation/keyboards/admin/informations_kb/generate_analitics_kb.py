from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.employees_kb.back_employees_kb import BackEmployeesNavigation
from presentation.keyboards.admin.informations_kb.back_informations_kb import BackInformationsNavigation


class GenerateAnalitics(CallbackData, prefix="GenerateAnalitics"):
    pass


class ConfirmationGenerateAnalitics(CallbackData, prefix="ConfirmationGenerateAnalitics"):
    pass


kb_confirmation_generate_analitics = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.GENERAL.CONFIRMATION(), callback_data=ConfirmationGenerateAnalitics().pack())],
    [InlineKeyboardButton(text=L.GENERAL.BACK(), callback_data=BackInformationsNavigation().pack())]
])
