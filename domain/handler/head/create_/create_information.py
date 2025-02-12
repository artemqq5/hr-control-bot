from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.constants import ROLE_HEAD
from data.repository.EmployeeRepository import EmployeeRepository
from data.repository.InformationRepository import InformationRepository
from data.repository.UserRepository import UserRepository
from domain.middleware.RoleMiddleware import RoleMiddleware
from domain.states.head.CreateInformState import CreateInformState
from presentation.keyboards.head.create_inform_kb.choice_employees_nav_kb import *
from presentation.keyboards.head.create_inform_kb.confirmation_create_info_kb import kb_confirmation_create_inform, \
    ConfirmationCreateInform

router = Router()

router.message.middleware(RoleMiddleware(ROLE_HEAD))
router.callback_query.middleware(RoleMiddleware(ROLE_HEAD))


@router.callback_query(ChoicedEmployee.filter())
async def choiced_employee_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    employee_id = int(callback.data.split(":")[1])
    employee = EmployeeRepository().employee(employee_id)
    await state.update_data(employee=employee)

    await state.set_state(CreateInformState.Describe)
    await callback.message.edit_text(i18n.HEAD.INFORMATION.CREATE.DESCRIBE())


@router.message(CreateInformState.Describe)
async def set_inform_desc(message: Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(desc=message.text)
    data = await state.get_data()
    await message.answer(
        i18n.HEAD.INFORMATION.CREATE.CONFIRMATION(
            employee_name=data['employee']['employee_name'],
            desc=data['desc']
        ), reply_markup=kb_confirmation_create_inform
    )


@router.callback_query(ConfirmationCreateInform.filter(), CreateInformState.Describe)
async def confirmation_create_inform_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(None)
    await callback.message.delete()

    data = await state.get_data()
    employee = data['employee']

    user = UserRepository().user(callback.from_user.id)

    if not InformationRepository().create(
            employee['employee_id'],
            employee['employee_name'],
            data['desc'],
            callback.from_user.id,
            callback.from_user.username,
            user['realname']
    ):
        await callback.message.answer(i18n.HEAD.INFORMATION.CREATE.FAIL())
        return

    await callback.message.answer(i18n.HEAD.INFORMATION.CREATE.SUCCESS())
