ADMIN-HEADS_ACCESS = Managers & Access 👥
ADMIN-EMPLOYEES = Employees 👨‍💼
ADMIN-INFORMATIONS = Informations 📑

# Accesses
ADMIN-ACCESS-GENERATE = 🔑 Generate Access
ADMIN-ACCESS-GENERATE-NAME = 📝 Enter user's name and position to understand who is requesting access:
ADMIN-ACCESS-GENERATE-CONFIRMATION = ✅ Confirm access generation for (<b>{$realname}</b>)?
ADMIN-ACCESS-GENERATE-FAIL = ❌ Failed to generate access!
ADMIN-ACCESS-GENERATE-SUCCESS = ✅ Link successfully created! Valid for 3 hours!
    🔗 Send this link to the person who needs access (just click to copy):
    <code>{$deeplink}</code>
ADMIN-USER-DESCIPTION = 👤 <b>{$realname}</b>
    =============================
    🆔 ID: <code>{$user_id}</code>
    📛 UserName: {$username}
    📅 Joined: {$join}
ADMIN-ACCESS-DELETE = ❌ Remove Access
ADMIN-ACCESS-DELETE-CONFIRMATION = 🚨 Access for <b>({$realname})</b> will be removed!
    🔹 All data will remain in the database, but synchronization will NOT occur if access is restored.
ADMIN-ACCESS-DELETE-SUCCESS = ✅ Access for (<b>{$realname}</b>) successfully removed!
ADMIN-ACCESS-DELETE-FAIL = ❌ Failed to remove access for (<b>{$realname}</b>)

# Employees
ADMIN-EMPLOYEE-ADD = ➕ Add Employee
ADMIN-EMPLOYEE-ADD-NAME = 👤 Employee name and short position title (e.g., Roman, Team Lead)
ADMIN-EMPLOYEE-ADD-POSITION = 📌 Position or responsibility area (detailed description):
ADMIN-EMPLOYEE-ADD-CONFIRMATION = ✅ Confirm employee addition?
    👤 Name: <b>{$employee_name}</b>
    📌 Position: <b>{$employee_position}</b>
ADMIN-EMPLOYEE-ADD-FAIL = ❌ Failed to add employee!
ADMIN-EMPLOYEE-ADD-SUCCESS = ✅ Employee successfully added!
ADMIN-EMPLOYEE-DESC = 👤 <b>{$employee_name}</b> | 🆔 ID: <b>{$employee_id}</b>
    =============================
    📌 Position: <b>{$employee_position}</b>
ADMIN-EMPLOYEE-DELETE = 🗑 Remove Employee
ADMIN-EMPLOYEE-DELETE-CONFIRMATION = ⚠️ Remove employee (<b>{$employee_name}</b>) from the database?
    🔹 All details will remain, but bot linking will be permanently lost!
ADMIN-EMPLOYEE-DELETE-SUCCESS = ✅ Employee (<b>{$employee_name}</b>) successfully removed!
ADMIN-EMPLOYEE-DELETE-FAIL = ❌ Failed to remove employee (<b>{$employee_name}</b>)

# Informations
ADMIN-INFORMATION-REPORT = 📊 Generate Report
ADMIN-INFORMATION-REPORT-CONFIRMATION = 📝 Export <code>analitics.xlsx</code> with all current records?
ADMIN-INFORMATION-REPORT-ERROR-NO_INFO = ⚠️ No data available for report generation!
ADMIN-INFORMATION-REPORT-SUCCESS = ✅ Successfully generated, here is your file 📂
ADMIN-INFORMATION-REPORT-FAIL = ❌ Failed to generate report!
ADMIN-INFORMATION-DESC = 📄 Information <b>#{$id}</b> for <b>{$employee_name}</b>
    =============================
    📋 {$desc}

    🏷 From: <b>{$realname}</b> ({$username})
    📅 Date: <b>{$created}</b>
