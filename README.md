[Advanced CRUD app with Authentication]
A robust Django web application featuring a product CRUD system, student/employee management, and automated user profiling and a well structured admin panel using relationships.

🚀 Features:
Authentication: Secure Login, Logout, and User Registration.
Automated Profiles: Used Django Signals to automatically create a User Profile upon registration.
Product Management: Full CRUD (Create, Read, Update, Delete) functionality for products.
Role-Based Views: * Students: Can view their academic marks.
Employees: Can register themselves and manage their data.
Admin Panel: Full administrative control over all database entries.
🛠️ Tech Stack
Backend: Django (Python)
Database: SQLite (Development)
Frontend: Html,Css,bootstrap
📋 How to Install and Run
Clone the repository:

git clone [https://github.com/](https://github.com/)[mk567]/[1st-repository].git
create virtual environment Python -m venv venv source venv/bin activate #on windows: venv/Scripts/activate

Install requirements ** pip Install -r requirements.txt **

Run migrations ** Python manage.py make migrations Python manage.py migrate **

Start the server ** Python manage.py runserver **
