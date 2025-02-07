import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore

import config
from domain.handler.admin import admin_handler
from domain.handler.head import head_handler
from domain.handler.no_register import no_register_handler
from domain.middleware.IsUserRegisteredMiddleware import IsUserRegisteredMiddleware
from domain.middleware.LocaleManager import LocaleManager

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_routers(
    no_register_handler.router,
    admin_handler.router,
    head_handler.router,
)


async def main():
    # logs
    logging.basicConfig(level=logging.INFO)

    # bot settings
    default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=config.BOT_TOKEN, default=default_properties, timeout=60)

    try:
        # localization middleware
        i18n_middleware = I18nMiddleware(
            core=FluentRuntimeCore(path='presentation/locales'),
            default_locale='en',
            manager=LocaleManager()
        )

        i18n_middleware.setup(dp)

        dp.message.outer_middleware(IsUserRegisteredMiddleware())  # check if user not registered
        dp.callback_query.outer_middleware(IsUserRegisteredMiddleware())  # check if user not registered

        # start bot
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        print(f"start hr bot: {e}")
        return


if __name__ == '__main__':
    asyncio.run(main())
