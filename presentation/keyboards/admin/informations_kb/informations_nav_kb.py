import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from presentation.keyboards.admin.informations_kb.generate_analitics_kb import GenerateAnalitics


class InformationDescription(CallbackData, prefix="InformationDescription"):
    id: int


class InformationsNavigation(CallbackData, prefix="InformationsNavigation"):
    page: int


def kb_informations_managment(informations, current_page: int = 1):
    inline_kb = [[InlineKeyboardButton(
        text=L.ADMIN.INFORMATION.REPORT(),
        callback_data=GenerateAnalitics().pack()
    )]]

    # if items less then pages exist before -> Leave to 1 page
    if len(informations) < (current_page * 15) - 14:
        current_page = 1

    total_pages = math.ceil(len(informations) / 15)
    start_index = (current_page - 1) * 15
    end_index = min(start_index + 15, len(informations))

    # load from db
    for i in range(start_index, end_index):
        inline_kb.append(
            [InlineKeyboardButton(
                text=f"#{informations[i]['id']} {informations[i]['employee_name']} - {informations[i]['desc']}",
                callback_data=InformationDescription(id=informations[i]['id']).pack()
            )]
        )

    if len(informations) > 15:
        nav = []

        if current_page > 1:
            nav.append(InlineKeyboardButton(
                text='◀️',
                callback_data=InformationsNavigation(page=current_page - 1).pack()
            ))

        nav.append(InlineKeyboardButton(text=f"{current_page}/{total_pages}", callback_data="None"))

        if current_page < total_pages:
            nav.append(InlineKeyboardButton(
                text='▶️',
                callback_data=InformationsNavigation(page=current_page + 1).pack()
            ))

        inline_kb.append(nav)

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)
