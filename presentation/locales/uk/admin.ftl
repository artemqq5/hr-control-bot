ADMIN-HEADS_ACCESS = Керівники та доступи
ADMIN-EMPLOYEES = Працівники
ADMIN-INFORMATIONS = Відомості

# Accesses
ADMIN-ACCESS-GENERATE = Створити доступ
ADMIN-ACCESS-GENERATE-NAME = Ім'я та посада користувача, щоб розуміти від кого надішов запит:
ADMIN-ACCESS-GENERATE-CONFIRMATION = Підтвердити генерацію доступу для (<b>{$realname}</b>)?
ADMIN-ACCESS-GENERATE-FAIL = Помилка при генерації доступа ❌
ADMIN-ACCESS-GENERATE-SUCCESS = Посилання успішно створено ✅ Діє 3 години!
    Надішліть це посилання людині, котра має отримати доступ 🔗 (просто натисінть щоб скопіювати):
    <code>{$deeplink}</code>
ADMIN-USER-DESCIPTION = 👤 <b>{$realname}</b>
    =============================
    ID: <code>{$user_id}</code>
    UserName: {$username}
    Join: {$join}
ADMIN-ACCESS-DELETE = Видалити доступ
ADMIN-ACCESS-DELETE-CONFIRMATION = Доступ для <b>({$realname})</b> буде видалено, але всі дані залишаться в базі, якщо доступ буде поновлено дані не синхронізуються
ADMIN-ACCESS-DELETE-SUCCESS = Доступ для користувача (<b>{$realname}</b>) видалено успішно ✅
ADMIN-ACCESS-DELETE-FAIL = Не вдалося видалити доступ для користувача (<b>{$realname}</b>) ❌

# Employees
ADMIN-EMPLOYEE-ADD = Додати працівника
ADMIN-EMPLOYEE-ADD-NAME = Ім'я працівника з короткою назвою посади, наприклад (Роман, Тімлід):
ADMIN-EMPLOYEE-ADD-POSITION = Позиція\посада або зона відповідальності працівника, розгорнутий опис:
ADMIN-EMPLOYEE-ADD-CONFIRMATION = Підтвердити додавання працівника?
    Ім'я: <b>{$employee_name}</b>
    Позиція: <b>{$employee_position}</b>
ADMIN-EMPLOYEE-ADD-FAIL = Помилка додавання працівника ❌
ADMIN-EMPLOYEE-ADD-SUCCESS = Працівника успішно додано! ✅
ADMIN-EMPLOYEE-DESC = 👤 <b>{$employee_name}</b> | ID: <b>{$employee_id}</b>
    =============================
    Позиція: <b>{$employee_position}</b>
ADMIN-EMPLOYEE-DELETE = Видалити працівника
ADMIN-EMPLOYEE-DELETE-CONFIRMATION = Видалити працівника (<b>{$employee_name}</b>) з бази? Всі відомості щодо нього залишаться в базі, але прив'язка у боті буде втрачена назавжди!
ADMIN-EMPLOYEE-DELETE-SUCCESS = Працівника (<b>{$employee_name}</b>) видалено успішно ✅
ADMIN-EMPLOYEE-DELETE-FAIL = Не вдалося видалити працівника (<b>{$employee_name}</b>) ❌

# Informations
ADMIN-INFORMATION-DESC = Відомість <b>#{$id}</b> по <b>{$realname}</b>
    =============================
    {$desc}

    Дата: <b>{$created}</b>

