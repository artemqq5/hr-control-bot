from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.employees_kb.back_employees_kb import BackEmployeesNavigation


class DeleteEmployee(CallbackData, prefix="DeleteEmployee"):
    pass


class ConfirmationDeleteEmployee(CallbackData, prefix="ConfirmationDeleteEmployee"):
    pass


kb_confirmation_delete_employee = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.GENERAL.CONFIRMATION(), callback_data=ConfirmationDeleteEmployee().pack())],
    [InlineKeyboardButton(text=L.GENERAL.BACK(), callback_data=BackEmployeesNavigation().pack())]
])
