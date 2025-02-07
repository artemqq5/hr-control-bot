from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.constants import ROLE_ADMIN
from data.repository.UserRepository import UserRepository
from domain.middleware.RoleMiddleware import RoleMiddleware
from presentation.keyboards.admin.access_kb.back_access_kb import kb_back_users_nav
from presentation.keyboards.admin.access_kb.delete_access_kb import DeleteAccess, ConfirmationDeleteAccess, \
    kb_confirmation_delete_access

router = Router()

router.message.middleware(RoleMiddleware(ROLE_ADMIN))
router.callback_query.middleware(RoleMiddleware(ROLE_ADMIN))


@router.callback_query(DeleteAccess.filter())
async def delete_access_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    await callback.message.edit_text(i18n.ACCESS.DELETE.CONFIRMATION(
        realname=data['user']['realname']),
        reply_markup=kb_confirmation_delete_access
    )


@router.callback_query(ConfirmationDeleteAccess.filter())
async def confirmation_delete_access_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await callback.message.delete()

    data = await state.get_data()

    if not UserRepository().delete_user_role(data['user']['user_id']):
        await callback.message.answer(
            i18n.ACCESS.DELETE.FAIL(realname=data['user']['realname']),
            reply_markup=kb_back_users_nav
        )
        return

    await callback.message.answer(
        i18n.ACCESS.DELETE.SUCCESS(realname=data['user']['realname']),
        reply_markup=kb_back_users_nav
    )
