from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.employees_kb.back_employees_kb import BackEmployeesNavigation


class AddEmployee(CallbackData, prefix="AddEmployee"):
    pass


class ConfirmationAddEmployee(CallbackData, prefix="ConfirmationAddEmployee"):
    pass


kb_confirmation_add_employee = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.CONFIRMATION(), callback_data=ConfirmationAddEmployee().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackEmployeesNavigation().pack())]
])
