from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.constants import ROLE_ADMIN
from data.repository.EmployeeRepository import EmployeeRepository
from domain.middleware.RoleMiddleware import RoleMiddleware
from presentation.keyboards.admin.employees_kb.back_employees_kb import kb_back_employees_nav
from presentation.keyboards.admin.employees_kb.delete_employee_kb import *

router = Router()

router.message.middleware(RoleMiddleware(ROLE_ADMIN))
router.callback_query.middleware(RoleMiddleware(ROLE_ADMIN))


@router.callback_query(DeleteEmployee.filter())
async def delete_employee_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    await callback.message.edit_text(i18n.EMPLOYEE.DELETE.CONFIRMATION(
        employee_name=data['employee']['employee_name']),
        reply_markup=kb_confirmation_delete_employee
    )


@router.callback_query(ConfirmationDeleteEmployee.filter())
async def confirmation_delete_employee_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await callback.message.delete()

    data = await state.get_data()

    if not EmployeeRepository().delete_employee(data['employee']['employee_id']):
        await callback.message.answer(
            i18n.EMPLOYEE.DELETE.FAIL(employee_name=data['employee']['employee_name']),
            reply_markup=kb_back_employees_nav
        )
        return

    await callback.message.answer(
        i18n.EMPLOYEE.DELETE.SUCCESS(employee_name=data['employee']['employee_name']),
        reply_markup=kb_back_employees_nav
    )
