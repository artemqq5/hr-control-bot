ADMIN-HEADS_ACCESS = Руководители и доступы 👥
ADMIN-EMPLOYEES = Сотрудники 👨‍💼
ADMIN-INFORMATIONS = Ведомости 📑

# Доступы
ADMIN-ACCESS-GENERATE = 🔑 Создать доступ
ADMIN-ACCESS-GENERATE-NAME = 📝 Введите имя и должность пользователя, чтобы понимать, кто запрашивает доступ:
ADMIN-ACCESS-GENERATE-CONFIRMATION = ✅ Подтвердить создание доступа для (<b>{$realname}</b>)?
ADMIN-ACCESS-GENERATE-FAIL = ❌ Ошибка при создании доступа!
ADMIN-ACCESS-GENERATE-SUCCESS = ✅ Ссылка успешно создана! Действует 3 часа!
    🔗 Отправьте эту ссылку человеку, которому нужен доступ (просто нажмите, чтобы скопировать):
    <code>{$deeplink}</code>
ADMIN-USER-DESCIPTION = 👤 <b>{$realname}</b>
    =============================
    🆔 ID: <code>{$user_id}</code>
    📛 Имя пользователя: {$username}
    📅 Дата входа: {$join}
ADMIN-ACCESS-DELETE = ❌ Удалить доступ
ADMIN-ACCESS-DELETE-CONFIRMATION = 🚨 Доступ для <b>({$realname})</b> будет удалён!
    🔹 Все данные останутся в базе, но при повторном доступе синхронизация НЕ произойдёт.
ADMIN-ACCESS-DELETE-SUCCESS = ✅ Доступ для (<b>{$realname}</b>) успешно удалён!
ADMIN-ACCESS-DELETE-FAIL = ❌ Не удалось удалить доступ для (<b>{$realname}</b>)

# Сотрудники
ADMIN-EMPLOYEE-ADD = ➕ Добавить сотрудника
ADMIN-EMPLOYEE-ADD-NAME = 👤 Имя сотрудника и краткое название должности (например, Роман, Тимлид)
ADMIN-EMPLOYEE-ADD-POSITION = 📌 Должность или зона ответственности (развернутое описание):
ADMIN-EMPLOYEE-ADD-CONFIRMATION = ✅ Подтвердить добавление сотрудника?
    👤 Имя: <b>{$employee_name}</b>
    📌 Должность: <b>{$employee_position}</b>
ADMIN-EMPLOYEE-ADD-FAIL = ❌ Ошибка при добавлении сотрудника!
ADMIN-EMPLOYEE-ADD-SUCCESS = ✅ Сотрудник успешно добавлен!
ADMIN-EMPLOYEE-DESC = 👤 <b>{$employee_name}</b> | 🆔 ID: <b>{$employee_id}</b>
    =============================
    📌 Должность: <b>{$employee_position}</b>
ADMIN-EMPLOYEE-DELETE = 🗑 Удалить сотрудника
ADMIN-EMPLOYEE-DELETE-CONFIRMATION = ⚠️ Удалить сотрудника (<b>{$employee_name}</b>) из базы?
    🔹 Вся информация останется, но привязка в боте будет потеряна навсегда!
ADMIN-EMPLOYEE-DELETE-SUCCESS = ✅ Сотрудник (<b>{$employee_name}</b>) успешно удалён!
ADMIN-EMPLOYEE-DELETE-FAIL = ❌ Не удалось удалить сотрудника (<b>{$employee_name}</b>)

# Отчёты
ADMIN-INFORMATION-REPORT = 📊 Создать отчёт
ADMIN-INFORMATION-REPORT-CONFIRMATION = 📝 Выгрузить <code>analitics.xlsx</code> со всеми текущими данными?
ADMIN-INFORMATION-REPORT-ERROR-NO_INFO = ⚠️ Нет данных для создания отчёта!
ADMIN-INFORMATION-REPORT-SUCCESS = ✅ Отчёт успешно создан, вот ваш файл 📂
ADMIN-INFORMATION-REPORT-FAIL = ❌ Не удалось создать отчёт!
ADMIN-INFORMATION-DESC = 📄 Ведомость <b>#{$id}</b> по <b>{$employee_name}</b>
    =============================
    📋 {$desc}

    🏷 Отправитель: <b>{$realname}</b> ({$username})
    📅 Дата: <b>{$created}</b>
