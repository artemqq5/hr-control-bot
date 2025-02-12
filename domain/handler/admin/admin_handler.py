from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext, L

from data.constants import ROLE_ADMIN
from data.repository.EmployeeRepository import EmployeeRepository
from data.repository.InformationRepository import InformationRepository
from data.repository.UserRepository import UserRepository
from domain.filter.RoleFilter import RoleFilter
from domain.handler.admin.accesses_ import nav_access
from domain.handler.admin.employees_ import nav_employees
from domain.handler.admin.informations_ import nav_informations
from domain.middleware.RoleMiddleware import RoleMiddleware
from presentation.keyboards.admin.access_kb.access_nav_kb import kb_users_managment
from presentation.keyboards.admin.employees_kb.employees_nav_kb import kb_employees_managment
from presentation.keyboards.admin.general_admin_kb import kb_menu_admin
from presentation.keyboards.admin.informations_kb.informations_nav_kb import kb_informations_managment

router = Router()

router.include_routers(
    nav_access.router,
    nav_employees.router,
    nav_informations.router
)

router.message.middleware(RoleMiddleware(ROLE_ADMIN))
router.callback_query.middleware(RoleMiddleware(ROLE_ADMIN))


@router.message(Command("start"), RoleFilter(ROLE_ADMIN))
async def start(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(i18n.GENERAL.MENU(), reply_markup=kb_menu_admin)


@router.message(F.text == L.ADMIN.HEADS_ACCESS())
async def accesses(message: Message, i18n: I18nContext, state: FSMContext):
    users_list = UserRepository().registered_users()
    await message.answer(i18n.ADMIN.HEADS_ACCESS(), reply_markup=kb_users_managment(users_list))


@router.message(F.text == L.ADMIN.EMPLOYEES())
async def employees(message: Message, i18n: I18nContext, state: FSMContext):
    employee_list = EmployeeRepository().employees()
    await message.answer(i18n.ADMIN.EMPLOYEES(), reply_markup=kb_employees_managment(employee_list))


@router.message(F.text == L.ADMIN.INFORMATIONS())
async def informations(message: Message, i18n: I18nContext, state: FSMContext):
    information_list = InformationRepository().informations()
    await message.answer(
        text=i18n.ADMIN.INFORMATIONS(),
        reply_markup=kb_informations_managment(information_list)
    )
    pass
