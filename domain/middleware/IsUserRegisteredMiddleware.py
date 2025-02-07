from typing import Callable, Any, Dict, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject

from data.repository.UserRepository import UserRepository


class IsUserRegisteredMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if not isinstance(event, (types.Message, types.CallbackQuery)):
            return

        user = event.from_user

        if not UserRepository().user(user.id):
            UserRepository().add_user(user.id, user.first_name, user.username, user.language_code)

        return await handler(event, data)
