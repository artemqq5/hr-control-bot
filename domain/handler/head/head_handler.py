from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext, L

from data.constants import ROLE_HEAD
from data.repository.InformationRepository import InformationRepository
from domain.filter.RoleFilter import RoleFilter
from domain.handler.head.nav_informations_ import nav_my_informations
from domain.middleware.RoleMiddleware import RoleMiddleware
from presentation.keyboards.head.general_head_kb import kb_menu_head
from presentation.keyboards.head.my_information_kb.my_informations_nav_kb import kb_my_informations_managment

router = Router()

router.include_routers(nav_my_informations.router)

router.message.middleware(RoleMiddleware(ROLE_HEAD))
router.callback_query.middleware(RoleMiddleware(ROLE_HEAD))


@router.message(Command("start"), RoleFilter(ROLE_HEAD))
async def start(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(i18n.GENERAL.MENU(), reply_markup=kb_menu_head)


@router.message(F.text == L.HEAD.INFORMATIONS(), RoleFilter(ROLE_HEAD))
async def my_informations(message: Message, i18n: I18nContext, state: FSMContext):
    information_list = InformationRepository().informations()
    await message.answer(
        text=i18n.HEAD.INFORMATIONS(),
        reply_markup=kb_my_informations_managment(information_list)
    )
