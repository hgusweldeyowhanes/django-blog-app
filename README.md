1. Create & activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
2. Install dependencies
  pip install python 3.13
  pip install Django
  pip install djangorestframework
3. Apply migrations & run server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
4. Access the app
Go to: http://127.0.0.1:8000
5. Screenshot


# 🗨️ Django RoomChat

A real-time RoomChat application built with Django. Users can create chat rooms, join discussions, and post messages. Ideal for small communities, study groups, or team collaboration.


## 🚀 Features

- ✅ Create, join, and delete chat rooms
- 💬 Post messages in real-time 
- 🔍 Filter/search rooms by topic or name
- 👤 Basic user authentication (Login/Register)
- 🧩 Django REST Framework API (optional)

## 🛠️ Technologies Used

- Python 3.x
- Django
- SQLite (default)
- HTML/CSS
- Django REST Framework 
- Git & GitHub

---

## 📂 Project Structure
RoomChat/  called  product  
├── project/              # Django project settings
│   └── settings.py
├── chat/                 # Main app: models, views, urls
│   ├── models.py
│   ├── views.py
│   ├── templates/
├── static/               # CSS, JS, etc.
├── manage.py
├── .gitignore
└── README.md
