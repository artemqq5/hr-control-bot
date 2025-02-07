from typing import Optional

from aiogram.filters import BaseFilter
from aiogram.types import Message

from data.repository.UserRepository import UserRepository


class RoleFilter(BaseFilter):

    def __init__(self, role: Optional[str] = 'admin'):
        self.role = role

    async def __call__(self, message: Message):
        return UserRepository().user(message.from_user.id).get('user_role', None) == self.role
