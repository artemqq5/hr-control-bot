from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext

from data.repository.UserRepository import UserRepository
from data.transaction.AccessTransactions import AccessTransactions
from domain.filter.RoleFilter import RoleFilter
from domain.middleware.RoleMiddleware import RoleMiddleware

router = Router()

router.message.middleware(RoleMiddleware(None))
router.callback_query.middleware(RoleMiddleware(None))


@router.message(Command("start"), RoleFilter(None))
async def start_deeplink(message: Message, command: CommandObject, state: FSMContext, i18n: I18nContext):
    join_key = command.args
    user = message.from_user

    if not join_key:
        await message.answer(text=i18n.GENERAL.IS_NOT_REGISTERED())
        return

    activate_access = AccessTransactions().register_user_transaction(user.id, user.username, join_key, i18n)

    if not activate_access['result']:
        await message.answer(text=activate_access['error'])
        return

    await message.answer(i18n.HEAD.REGISTER_SUCCESS())


@router.message(RoleFilter(None))
async def messages(message: Message, state: FSMContext, i18n: I18nContext):
    if not UserRepository().user(message.from_user.id).get('role'):
        await message.answer(text=i18n.GENERAL.IS_NOT_REGISTERED())
