# Intelligent Hospital Management System

A Django-based Hospital Management System developed to streamline hospital operations.

## Features
- **Admin Panel**: Manage departments, doctors, and hospitals.
- **Hospital Panel**: Manage doctors, schedules, and appointments.
- **Doctor Panel**: View appointments, manage schedules, and prescribe medication.
- **User Panel**: Book appointments, view doctors, and manage profile.

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/athulmurali667/intelligent-hospital-managementsystem.git
   cd intelligent-hospital-managementsystem
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django mysqlclient
   ```

4. **Database Configuration**
   - The project is currently configured to use **SQLite** by default for ease of setup.
   - If you wish to use **MySQL**, update `intelligent_hospital_managementsystem/settings.py` to uncomment the MySQL database configuration and configure your MySQL credentials.

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```
   Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Admin Credentials
To access the admin interface at `/admin`, use the following credentials:
- **Username**: `admin`
- **Password**: `admin`

## Troubleshooting
- **CSRF Verification Failed**: If you encounter this on the login page, simply refresh the page to generate a new CSRF cookie.
