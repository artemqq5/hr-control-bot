from typing import Callable, Any, Dict, Awaitable, Optional

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject

from data.repository.UserRepository import UserRepository


class RoleMiddleware(BaseMiddleware):

    def __init__(self, *roles: Optional[str]):
        self.role = list(roles)

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if not isinstance(event, (types.Message, types.CallbackQuery)):
            return

        user_id = event.from_user.id

        if UserRepository().user(user_id).get('user_role', None) in self.role:
            return await handler(event, data)

