from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext, L

from data.constants import ROLE_ADMIN, ROLE_HEAD
from data.repository.EmployeeRepository import EmployeeRepository
from domain.handler.admin_head.create_ import create_information
from domain.middleware.RoleMiddleware import RoleMiddleware
from domain.states.general.CreateInformState import CreateInformState
from presentation.keyboards.admin_head.create_inform_kb.choice_employees_nav_kb import kb_employees_choice

router = Router()

router.include_routers(create_information.router)

router.message.middleware(RoleMiddleware(ROLE_ADMIN, ROLE_HEAD))
router.callback_query.middleware(RoleMiddleware(ROLE_ADMIN, ROLE_HEAD))


@router.message(F.text == L.GENERAL.INFORMATION.CREATE())
async def create(message: Message, i18n: I18nContext, state: FSMContext):
    await state.set_state(CreateInformState.Employee)
    employee_list = EmployeeRepository().employees()
    await message.answer(
        i18n.GENERAL.INFORMATION.CREATE.CHOICE_EMPLOYEE(),
        reply_markup=kb_employees_choice(employee_list)
    )
