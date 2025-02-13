from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.constants import ROLE_HEAD
from data.repository.InformationRepository import InformationRepository
from domain.middleware.RoleMiddleware import RoleMiddleware
from presentation.keyboards.head.my_information_kb.back_my_informations_kb import *
from presentation.keyboards.head.my_information_kb.my_informations_nav_kb import *

router = Router()

router.message.middleware(RoleMiddleware(ROLE_HEAD))
router.callback_query.middleware(RoleMiddleware(ROLE_HEAD))


@router.callback_query(MyInformationsNavigation.filter())
async def my_informations_nav_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])

    await state.update_data(last_page_my_informations=page)
    information_list = InformationRepository().informations()

    await callback.message.edit_text(
        text=i18n.HEAD.INFORMATIONS(),
        reply_markup=kb_my_informations_managment(information_list, current_page=page)
    )


@router.callback_query(MyInformationDescription.filter())
async def my_information_description_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    _id = int(callback.data.split(":")[1])
    information = InformationRepository().information(_id)

    await callback.message.edit_text(
        i18n.HEAD.INFORMATION.DESC(
            id=information['id'],
            employee_name=information['employee_name'],
            desc=information['desc'],
            created=str(information['created'])
        ),
        reply_markup=kb_back_my_informations_nav
    )


@router.callback_query(BackMyInformationsNavigation.filter())
async def informations_back_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await callback.message.delete()

    data = await state.get_data()
    information_list = InformationRepository().informations()

    await callback.message.answer(
        text=i18n.HEAD.INFORMATIONS(),
        reply_markup=kb_my_informations_managment(
            information_list,
            current_page=data.get('last_page_my_informations', 1)
        )
    )
