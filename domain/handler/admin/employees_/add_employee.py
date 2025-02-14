from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.constants import ROLE_ADMIN
from data.repository.EmployeeRepository import EmployeeRepository
from domain.middleware.RoleMiddleware import RoleMiddleware
from domain.states.admin.AddEmployeeState import AddEmployeeState
from presentation.keyboards.admin.employees_kb.add_employee_kb import *
from presentation.keyboards.admin.employees_kb.back_employees_kb import kb_back_employees_nav

router = Router()

router.message.middleware(RoleMiddleware(ROLE_ADMIN))
router.callback_query.middleware(RoleMiddleware(ROLE_ADMIN))


@router.callback_query(AddEmployee.filter())
async def add_employee_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddEmployeeState.Name)
    await callback.message.edit_text(i18n.ADMIN.EMPLOYEE.ADD.NAME(), reply_markup=kb_back_employees_nav)


@router.message(AddEmployeeState.Name)
async def set_employee_name(message: Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(name=message.text)
    data = await state.get_data()

    await message.answer(
        i18n.ADMIN.EMPLOYEE.ADD.CONFIRMATION(employee_name=data['name']),
        reply_markup=kb_confirmation_add_employee
    )


@router.callback_query(ConfirmationAddEmployee.filter())
async def confirmation_add_employee_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(None)
    await callback.message.delete()

    data = await state.get_data()

    if not EmployeeRepository().add_employee(data['name']):
        await callback.message.answer(i18n.ADMIN.EMPLOYEE.ADD.FAIL(), reply_markup=kb_back_employees_nav)
        return

    await callback.message.answer(
        i18n.ADMIN.EMPLOYEE.ADD.SUCCESS(),
        reply_markup=kb_back_employees_nav
    )
