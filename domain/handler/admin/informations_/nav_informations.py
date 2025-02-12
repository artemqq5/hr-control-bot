from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.constants import ROLE_ADMIN
from data.repository.InformationRepository import InformationRepository
from domain.handler.admin.informations_ import generate_analitics
from domain.middleware.RoleMiddleware import RoleMiddleware
from presentation.keyboards.admin.informations_kb.back_informations_kb import *
from presentation.keyboards.admin.informations_kb.informations_nav_kb import *

router = Router()

router.include_routers(
    generate_analitics.router
)

router.message.middleware(RoleMiddleware(ROLE_ADMIN))
router.callback_query.middleware(RoleMiddleware(ROLE_ADMIN))


@router.callback_query(InformationsNavigation.filter())
async def informations_nav_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])

    await state.update_data(last_page_informations=page)
    information_list = InformationRepository().informations()

    await callback.message.edit_text(
        text=i18n.ADMIN.INFORMATIONS(),
        reply_markup=kb_informations_managment(information_list, current_page=page)
    )


@router.callback_query(InformationDescription.filter())
async def information_description_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    _id = int(callback.data.split(":")[1])
    information = InformationRepository().information(_id)

    await callback.message.edit_text(
        i18n.ADMIN.INFORMATION.DESC(
            id=information['id'],
            employee_name=information['employee_name'],
            desc=information['desc'],
            realname=information['realname'],
            username=f"@{information['username']}" if information.get('username') else " ",
            created=str(information['created'])
        ),
        reply_markup=kb_back_informations_nav
    )


@router.callback_query(BackInformationsNavigation.filter())
async def informations_back_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await callback.message.delete()

    data = await state.get_data()
    information_list = InformationRepository().informations()

    await callback.message.answer(
        text=i18n.ADMIN.INFORMATIONS(),
        reply_markup=kb_informations_managment(information_list, current_page=data.get('last_page_informations', 1))
    )
