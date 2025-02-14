import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from presentation.keyboards.admin.employees_kb.add_employee_kb import AddEmployee
from presentation.keyboards.admin.employees_kb.back_employees_kb import BackEmployeesNavigation
from presentation.keyboards.admin.employees_kb.delete_employee_kb import DeleteEmployee


class EmployeesDescription(CallbackData, prefix="EmployeesDescription"):
    employee_id: int


kb_employee_detail = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.EMPLOYEE.DELETE(), callback_data=DeleteEmployee().pack())],
    [InlineKeyboardButton(text=L.GENERAL.BACK(), callback_data=BackEmployeesNavigation().pack())]
])


class EmployeesNavigation(CallbackData, prefix="EmployeesNavigation"):
    page: int


def kb_employees_managment(emmployes, current_page: int = 1):
    inline_kb = [[InlineKeyboardButton(
        text=L.ADMIN.EMPLOYEE.ADD(),
        callback_data=AddEmployee().pack()
    )]]

    # if items less then pages exist before -> Leave to 1 page
    if len(emmployes) < (current_page * 15) - 14:
        current_page = 1

    total_pages = math.ceil(len(emmployes) / 15)
    start_index = (current_page - 1) * 15
    end_index = min(start_index + 15, len(emmployes))

    # load from db
    for i in range(start_index, end_index):
        inline_kb.append(
            [InlineKeyboardButton(
                text=f"{emmployes[i]['employee_name']} #{emmployes[i]['employee_id']}",
                callback_data=EmployeesDescription(employee_id=emmployes[i]['employee_id']).pack()
            )]
        )

    if len(emmployes) > 15:
        nav = []

        if current_page > 1:
            nav.append(InlineKeyboardButton(
                text='◀️',
                callback_data=EmployeesNavigation(page=current_page - 1).pack()
            ))

        nav.append(InlineKeyboardButton(text=f"{current_page}/{total_pages}", callback_data="None"))

        if current_page < total_pages:
            nav.append(InlineKeyboardButton(
                text='▶️',
                callback_data=EmployeesNavigation(page=current_page + 1).pack()
            ))

        inline_kb.append(nav)

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)
