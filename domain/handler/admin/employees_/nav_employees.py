from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.constants import ROLE_ADMIN
from data.repository.EmployeeRepository import EmployeeRepository
from domain.handler.admin.employees_ import add_employee, delete_employee
from domain.middleware.RoleMiddleware import RoleMiddleware
from presentation.keyboards.admin.employees_kb.employees_nav_kb import *

router = Router()

router.include_routers(
    add_employee.router,
    delete_employee.router
)

router.message.middleware(RoleMiddleware(ROLE_ADMIN))
router.callback_query.middleware(RoleMiddleware(ROLE_ADMIN))


@router.callback_query(EmployeesNavigation.filter())
async def employees_nav_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])

    await state.update_data(last_page_employees=page)
    employee_list = EmployeeRepository().employees()

    await callback.message.edit_text(
        text=i18n.ADMIN.EMPLOYEES(),
        reply_markup=kb_employees_managment(employee_list, current_page=page)
    )


@router.callback_query(EmployeesDescription.filter())
async def user_description_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    employee_id = int(callback.data.split(":")[1])
    employee = EmployeeRepository().employee(employee_id)

    await state.update_data(employee=employee)

    await callback.message.edit_text(
        i18n.ADMIN.EMPLOYEE.DESC(
            employee_name=employee['employee_name'],
            employee_id=employee['employee_id'],
            employee_position=employee['employee_position'],
        ),
        reply_markup=kb_employee_detail
    )


@router.callback_query(BackEmployeesNavigation.filter())
async def employees_back_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    employee_list = EmployeeRepository().employees()

    await callback.message.edit_text(
        text=i18n.ADMIN.EMPLOYEES(),
        reply_markup=kb_employees_managment(employee_list, current_page=data.get('last_page_employees', 1))
    )
