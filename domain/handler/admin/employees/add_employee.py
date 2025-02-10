# import uuid
# from aiogram import Router
# from aiogram.fsm.context import FSMContext
# from aiogram.types import CallbackQuery, Message
# from aiogram_i18n import I18nContext
#
# from config import DEEPLINK
# from data.constants import ROLE_ADMIN
# from data.repository.AccessRepository import AccessRepository
# from domain.middleware.RoleMiddleware import RoleMiddleware
# from domain.states.admin.GenerateAccessState import GenerateAccessState
# from presentation.keyboards.admin.access_kb.back_access_kb import kb_back_users_nav
# from presentation.keyboards.admin.access_kb.generate_access_kb import GenerateAccess, ConfirmationGenerateAccess, \
#     kb_confirmation_generate_access
#
# router = Router()
#
# router.message.middleware(RoleMiddleware(ROLE_ADMIN))
# router.callback_query.middleware(RoleMiddleware(ROLE_ADMIN))
#
#
# @router.callback_query(GenerateAccess.filter())
# async def generate_access_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
#     await state.set_state(GenerateAccessState.RealName)
#     await callback.message.edit_text(i18n.ACCESS.GENERATE.NAME(), reply_markup=kb_back_users_nav)
#
#
# @router.message(GenerateAccessState.RealName)
# async def set_access_name(message: Message, state: FSMContext, i18n: I18nContext):
#     await state.update_data(realname=message.text)
#     await message.answer(
#         i18n.ACCESS.GENERATE.CONFIRMATION(realname=message.text),
#         reply_markup=kb_confirmation_generate_access
#     )
#
#
# @router.callback_query(ConfirmationGenerateAccess.filter(), GenerateAccessState.RealName)
# async def generate_access_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
#     await state.set_state(None)
#
#     data = await state.get_data()
#     access_uuid = uuid.uuid4()
#
#     if not AccessRepository().generate_access(access_uuid, data['realname']):
#         await callback.message.edit_text(i18n.ACCESS.GENERATE.FAIL(), reply_markup=kb_back_users_nav)
#         return
#
#     await callback.message.edit_text(
#         i18n.ACCESS.GENERATE.SUCCESS(deeplink=DEEPLINK.format(access_uuid)),
#         reply_markup=kb_back_users_nav
#     )
