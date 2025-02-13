import logging
from asyncio import gather

from aiogram import Bot
from aiogram_i18n import I18nContext

from data.repository.UserRepository import UserRepository


class AdminNotificationManager:

    @staticmethod
    async def user_created_information(data, user_id: int, bot: Bot, i18n: I18nContext):
        counter = 0

        admins = UserRepository().admins()
        user = UserRepository().user(user_id)

        async def notify_admin(admin):
            nonlocal counter
            try:
                with i18n.use_locale(admin.get('lang', 'en')):
                    await bot.send_message(
                        chat_id=admin['user_id'],
                        text=i18n.NOTIFICATION.USER.CREATED_INFORMATION(
                            realname=user['realname'],
                            employee_name=data['employee']['employee_name'],
                            desc=data['desc']
                        )
                    )
                    counter += 1
            except Exception as e:
                logging.error(f"Messaging: Failed to notify admin {admin['user_id']}: {e}")

        # Виконання надсилання повідомлень асинхронно всім адміністраторам
        await gather(*[notify_admin(admin) for admin in admins])
        logging.info(f"Messaging user_created_information {counter}/{len(admins)} admins successfully.")
