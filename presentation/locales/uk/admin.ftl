ADMIN-HEADS_ACCESS = Керівники та доступи 👥
ADMIN-EMPLOYEES = Працівники 👨‍💼
ADMIN-INFORMATIONS = Відомості 📑

# Accesses
ADMIN-ACCESS-GENERATE = 🔑 Створити доступ
ADMIN-ACCESS-GENERATE-NAME = 📝 Ім'я та посада користувача, щоб розуміти від кого надішов запит:
ADMIN-ACCESS-GENERATE-CONFIRMATION = ✅ Підтвердити генерацію доступу для (<b>{$realname}</b>)?
ADMIN-ACCESS-GENERATE-FAIL = ❌ Помилка при генерації доступу!
ADMIN-ACCESS-GENERATE-SUCCESS = ✅ Посилання успішно створено! Діє 3 години!
    🔗 Надішліть це посилання людині, котра має отримати доступ (просто натисніть, щоб скопіювати):
    <code>{$deeplink}</code>
ADMIN-USER-DESCIPTION = 👤 <b>{$realname}</b>
    =============================
    🆔 ID: <code>{$user_id}</code>
    📛 UserName: {$username}
    📅 Join: {$join}
ADMIN-ACCESS-DELETE = ❌ Видалити доступ
ADMIN-ACCESS-DELETE-CONFIRMATION = 🚨 Доступ для <b>({$realname})</b> буде видалено! Всі дані залишаться в базі, але синхронізація при повторному доступі НЕ відбудеться.
ADMIN-ACCESS-DELETE-SUCCESS = ✅ Доступ для користувача (<b>{$realname}</b>) успішно видалено!
ADMIN-ACCESS-DELETE-FAIL = ❌ Не вдалося видалити доступ для користувача (<b>{$realname}</b>)

# Employees
ADMIN-EMPLOYEE-ADD = ➕ Додати працівника
ADMIN-EMPLOYEE-ADD-NAME = 👤 Ім'я працівника та коротка назва посади, наприклад: (Роман, Тімлід)
ADMIN-EMPLOYEE-ADD-POSITION = 📌 Позиція або зона відповідальності працівника (розгорнутий опис):
ADMIN-EMPLOYEE-ADD-CONFIRMATION = ✅ Підтвердити додавання працівника?
    👤 Ім'я: <b>{$employee_name}</b>
    📌 Позиція: <b>{$employee_position}</b>
ADMIN-EMPLOYEE-ADD-FAIL = ❌ Помилка додавання працівника!
ADMIN-EMPLOYEE-ADD-SUCCESS = ✅ Працівника успішно додано!
ADMIN-EMPLOYEE-DESC = 👤 <b>{$employee_name}</b> | 🆔 ID: <b>{$employee_id}</b>
    =============================
    📌 Позиція: <b>{$employee_position}</b>
ADMIN-EMPLOYEE-DELETE = 🗑 Видалити працівника
ADMIN-EMPLOYEE-DELETE-CONFIRMATION = ⚠️ Видалити працівника (<b>{$employee_name}</b>) з бази?
    🔹 Всі відомості залишаться, але прив'язка у боті буде втрачена назавжди!
ADMIN-EMPLOYEE-DELETE-SUCCESS = ✅ Працівника (<b>{$employee_name}</b>) успішно видалено!
ADMIN-EMPLOYEE-DELETE-FAIL = ❌ Не вдалося видалити працівника (<b>{$employee_name}</b>)

# Informations
ADMIN-INFORMATION-REPORT = 📊 Генерувати звіт
ADMIN-INFORMATION-REPORT-CONFIRMATION = 📝 Вигрузити <code>analitics.xlsx</code> з усіма відомостями на даний момент?
ADMIN-INFORMATION-REPORT-ERROR-NO_INFO = ⚠️ Немає відомостей для генерації!
ADMIN-INFORMATION-REPORT-SUCCESS = ✅ Успішно згенеровано, ось ваш файл 📂
ADMIN-INFORMATION-REPORT-FAIL = ❌ Не вдалося згенерувати звіт!
ADMIN-INFORMATION-DESC = 📄 Відомість <b>#{$id}</b> по <b>{$employee_name}</b>
    =============================
    📋 {$desc}

    🏷 Від: <b>{$realname}</b> ({$username})
    📅 Дата: <b>{$created}</b>
