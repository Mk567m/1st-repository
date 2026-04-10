# [Advanced CRUD app with Authentication]

A robust Django web application featuring a product CRUD system, student/employee management, and automated user profiling and a well structured admin panel using relationships.

## 🚀 Features
* **Authentication:** Secure Login, Logout, and User Registration.
* **Automated Profiles:** Used Django Signals to automatically create a User Profile upon registration.
* **Product Management:** Full CRUD (Create, Read, Update, Delete) functionality for products.
* **Role-Based Views:** * **Students:** Can view their academic marks.
    * **Employees:** Can register themselves and manage their data.
* **Admin Panel:** Full administrative control over all database entries.

## 🛠️ Tech Stack
* **Backend:** Django (Python)
* **Database:** SQLite (Development)
* **Frontend:** Html,Css,bootstrap

## 📋 How to Install and Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/mk567/Django_projects

2.Install python/django and create virtual environment:
pip install django
Python -m venv venv
source venv/bin activate #on
windows: venv/Scripts/activate


3. Install requirements 
**
pip Install -r requirements.txt
**

4. Run migrations
**
Python manage.py make migrations

Python manage.py migrate
**

6. Start the server
**
Python manage.py runserver
**
