import logging
from datetime import datetime, timedelta

from aiogram_i18n import L

from data.repository.AccessRepository import AccessRepository
from data.repository.UserRepository import UserRepository
from data.transaction.repository.UserRepositoryTran import UserRepositoryTransaction


class AccessTransactions(UserRepositoryTransaction):

    def register_user_transaction(self, user_id, username, access_uuid, i18n):
        logging.info("Transaction start")
        logging.info(f"Data of transaction: (user_id:{user_id}, username:{username}, access_uuid:{access_uuid})")

        try:
            self._begin_transaction()

            access = self._access(access_uuid)
            if not access:
                logging.error("Access is not exist")
                raise Exception(i18n.ERROR.ACCESS_IS_NOT_AVAILABLE())

            if access.get('activated'):
                logging.error("Access has been register before")
                raise Exception(i18n.ERROR.ACCESS_HAD_ACTIVATED_BEFORE())

            if datetime.now() - access['created'] >= timedelta(hours=3):
                logging.error("Access created more then 3 hours ago")
                raise Exception(i18n.ERROR.ACCESS_HAD_CREATED_LONG_TIME_AGO())

            if not self._update_access(user_id, username, access_uuid):
                logging.error("Field to update access")
                raise Exception(i18n.ERROR.FAILED_ACTIVATE_ACCESS())

            if not self._update_user_status(access['user_role'], access['realname'], user_id):
                logging.error("Field to update user role")
                raise Exception(i18n.ERROR.FAILED_ACTIVATE_ACCESS())

            self._commit()
            return {"result": True}

        except Exception as e:
            self._rollback()
            logging.error(f"Transaction failed: {e}")
            return {"result": False, "error": str(e)}
        finally:
            self._close()
            logging.error("Transaction closed")
