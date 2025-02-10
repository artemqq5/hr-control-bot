from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.constants import ROLE_ADMIN
from data.repository.EmployeeRepository import EmployeeRepository
from domain.handler.admin.access_ import generate_access, delete_access
from domain.middleware.RoleMiddleware import RoleMiddleware
from presentation.keyboards.admin.employees_kb.employees_nav_kb import *

router = Router()

router.include_routers(
    # generate_access.router,
    # delete_access.router
)

router.message.middleware(RoleMiddleware(ROLE_ADMIN))
router.callback_query.middleware(RoleMiddleware(ROLE_ADMIN))


@router.callback_query(EmployeesNavigation.filter())
async def employees_nav_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])

    await state.update_data(last_page_employees=page)
    access_list = EmployeeRepository().employees()

    await callback.message.edit_text(
        text=i18n.ADMIN.HEADS_ACCESS(),
        reply_markup=kb_employees_managment(access_list, current_page=page)
    )


@router.callback_query(UsersDescription.filter())
async def user_description_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    user_id = int(callback.data.split(":")[1])
    user = EmployeeRepository().user(user_id)

    await state.update_data(user=user)

    await callback.message.edit_text(
        i18n.USER.DESCIPTION(
            realname=user['realname'],
            user_id=str(user['user_id']),
            username=f"@{user['username']}" if user.get('username') else "-",
            join=user['join']
        ),
        reply_markup=kb_user_detail
    )


@router.callback_query(BackUsersNavigation.filter())
async def employees_back_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    # access_list = EmployeeRepository().registered_employees()

    await callback.message.edit_text(
        text=i18n.ADMIN.HEADS_ACCESS(),
        reply_markup=kb_employees_managment(access_list, current_page=data.get('last_page_employees', 1))
    )
