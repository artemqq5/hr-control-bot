from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext

from data.constants import ROLE_HEAD
from domain.filter.RoleFilter import RoleFilter
from domain.middleware.RoleMiddleware import RoleMiddleware

router = Router()

router.message.middleware(RoleMiddleware(ROLE_HEAD))
router.callback_query.middleware(RoleMiddleware(ROLE_HEAD))


@router.message(Command("start"), RoleFilter(ROLE_HEAD))
async def start(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer("head")
