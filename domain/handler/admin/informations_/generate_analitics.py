from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile
from aiogram_i18n import I18nContext

from data.constants import ROLE_ADMIN
from data.repository.InformationRepository import InformationRepository
from domain.middleware.RoleMiddleware import RoleMiddleware
from domain.utilities.GenerateExelAnalitics import GenerateExcelAnalytics
from presentation.keyboards.admin.informations_kb.back_informations_kb import kb_back_informations_nav
from presentation.keyboards.admin.informations_kb.generate_analitics_kb import *

router = Router()

router.message.middleware(RoleMiddleware(ROLE_ADMIN))
router.callback_query.middleware(RoleMiddleware(ROLE_ADMIN))


@router.callback_query(GenerateAnalitics.filter())
async def generate_analitics_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await callback.message.edit_text(
        i18n.ADMIN.INFORMATION.REPORT.CONFIRMATION(),
        reply_markup=kb_confirmation_generate_analitics
    )


@router.callback_query(ConfirmationGenerateAnalitics.filter())
async def confirmation_generate_analitics_call(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(None)
    await callback.message.delete()

    informations = InformationRepository().informations()

    if not informations:
        await callback.message.answer(
            i18n.ADMIN.INFORMATION.REPORT.ERROR.NO_INFO(),
            reply_markup=kb_back_informations_nav)
        return

    document_analitics = GenerateExcelAnalytics().export(informations)

    if not document_analitics:
        await callback.message.answer(i18n.ADMIN.INFORMATION.REPORT.FAIL(), reply_markup=kb_back_informations_nav)
        return

    await callback.message.answer_document(
        document=FSInputFile(document_analitics),
        caption=i18n.ADMIN.INFORMATION.REPORT.SUCCESS(),
        reply_markup=kb_back_informations_nav
    )
