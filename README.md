#  Expense Tracker Web App

A **simple Expense Tracker web application** to track and manage your daily expenses, built using **Django + SQLite**, containerized using **Docker**, and ready for deployment on IBM Cloud.

---

##  Features

✅ Add, update, and delete expenses.  
✅ View your expenses by date and category.  
✅ Clean, minimal interface for daily tracking.  
✅ Dockerized for consistency across development and deployment.  
✅ Ready for IBM Cloud Container Registry and Code Engine deployment.

---

##  Technologies Used

- Python 3.9+
- Django
- SQLite
- Docker
- IBM Cloud (optional)

---

## 🛠 Local Installation

### 1️ Clone the repository
```cmd
git clone https://github.com/tejashxv/expense-tracker.git
cd expense-tracker
```

### 2 Install dependencies
```cmd
pip install -r requirements.txt
```
### 3 Run migrations
```cmd
python manage.py makemigrations
python manage.py migrate
```
### 4 Run the server
```cmd
python manage.py runserver
```
