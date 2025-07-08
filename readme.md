
# 🧑‍💼 Employee Manager

A simple and secure Django-based web application for managing employee records with **CRUD** operations and **staff-only access control**.

---

## 📌 Features

- Staff login-based access
- View all employee records
- Create new employee entries
- Edit/update existing employees
- View individual employee details
- Delete employee records with confirmation
- Clean UI using Django templates
- Access restricted to `is_staff` users only

---

## 🏗️ Project Structure

```

employee\_manager/
│
├── employee_manager/           # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── employees/                  # Custom app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── employees/
│           ├── employee_list.html
│           ├── employee_form.html
│           ├── employee_detail.html
│           └── confirm_delete.html
│
├── templates/                  # Project-level templates
│   └── login.html
    └── base.html
│
├── db.sqlite3                  # SQLite database
└── manage.py

````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
https://github.com/Rithika1406/Employee_Management-Djano-

cd employee_manager
````

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install django==5.2
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

> ⚠️ Superuser must have `is_staff = True` to access employee management views.

### 6. Run the Server

```bash
python manage.py runserver
```

Now open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Authentication & Authorization

* Access to all views is protected by `@login_required`
* Additionally restricted to `is_staff` users using `@user_passes_test(staff_required)`
* Login and logout handled via Django’s built-in auth system

---

## 🛣️ URL Endpoints

| URL Pattern         | View Function     | Description                    |
| ------------------- | ----------------- | ------------------------------ |
| `/`                 | `employee_list`   | List all employees             |
| `/create/`          | `employee_create` | Create new employee            |
| `/<int:pk>/`        | `employee_detail` | View employee detail           |
| `/<int:pk>/edit/`   | `employee_update` | Edit existing employee         |
| `/<int:pk>/delete/` | `employee_delete` | Delete employee (with confirm) |

---

## 📦 Requirements

* Python 3.10+
* Django 5.2
* SQLite (default)

---

## ✅ To Do (Optional Enhancements)

* Add pagination and search
* Add `is_active` status for employees
* Add employee profile pictures
* Add department and role fields
* Switch to PostgreSQL for production use

