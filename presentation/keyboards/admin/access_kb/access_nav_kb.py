import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from presentation.keyboards.admin.access_kb.back_access_kb import BackUsersNavigation
from presentation.keyboards.admin.access_kb.delete_access_kb import DeleteAccess
from presentation.keyboards.admin.access_kb.generate_access_kb import GenerateAccess


class UsersDescription(CallbackData, prefix="UsersDescription"):
    user_id: int


kb_user_detail = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ACCESS.DELETE(), callback_data=DeleteAccess().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackUsersNavigation().pack())]
])


class UsersNavigation(CallbackData, prefix="UsersNavigation"):
    page: int


def kb_users_managment(users, current_page: int = 1):
    inline_kb = [[InlineKeyboardButton(
        text=L.ACCESS.GENERATE(),
        callback_data=GenerateAccess().pack()
    )]]

    # if items less then pages exist before -> Leave to 1 page
    if len(users) < (current_page * 15) - 14:
        current_page = 1

    total_pages = math.ceil(len(users) / 15)
    start_index = (current_page - 1) * 15
    end_index = min(start_index + 15, len(users))

    # load from db
    for i in range(start_index, end_index):
        inline_kb.append(
            [InlineKeyboardButton(
                text=f"{users[i]['realname']}",
                callback_data=UsersDescription(user_id=users[i]['user_id']).pack()
            )]
        )

    if len(users) > 15:
        nav = []

        if current_page > 1:
            nav.append(InlineKeyboardButton(
                text='◀️',
                callback_data=UsersNavigation(page=current_page - 1).pack()
            ))

        nav.append(InlineKeyboardButton(text=f"{current_page}/{total_pages}", callback_data="None"))

        if current_page < total_pages:
            nav.append(InlineKeyboardButton(
                text='▶️',
                callback_data=UsersNavigation(page=current_page + 1).pack()
            ))

        inline_kb.append(nav)

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)
