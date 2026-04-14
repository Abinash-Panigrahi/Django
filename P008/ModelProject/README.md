# P008 — Django Models & MySQL Database Setup

## 📌 What This Project Covers
- Creating a Django Model (`Tshirt`) with fields: `name`, `brand`, `price`, `color`
- Connecting Django to a **MySQL database** instead of default SQLite
- Securing sensitive credentials using **`.env` file** with `python-dotenv`
- Running migrations to register the model in the database

---

## 🗂️ Project Structure

```
P008/
└── ModelProject/
    ├── ModelApp/
    │   ├── models.py        # Tshirt model definition
    │   ├── admin.py         # Default admin file (unused)
    │   └── ...
    ├── ModelProject/
    │   ├── settings.py      # Project settings (uses .env)
    │   ├── urls.py          # Only admin URL configured
    │   └── ...
    ├── .env                 # Secret credentials (NOT pushed to GitHub)
    ├── .env.example         # Template for environment variables
    └── manage.py
```

---

## 🧩 Model Used

```python
from django.db import models

class Tshirt(models.Model):
    name   = models.CharField(max_length=20)
    brand  = models.CharField(max_length=20)
    price  = models.IntegerField()
    color  = models.CharField(max_length=10)
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| Django | Web framework |
| MySQL | Database |
| python-dotenv | Environment variable management |
| mysqlclient | MySQL connector for Django |

---

## 🔐 Environment Variables

Copy `.env.example` to `.env` and fill in your actual credentials:

```bash
cp .env.example .env
```

> ⚠️ Never push your real `.env` file to GitHub. It is already covered in `.gitignore`.

---

## 🔧 Settings.py — Security Setup

```python
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 🚀 How to Run Locally

```bash
# 1. Activate virtual environment
.venv\Scripts\Activate.ps1              # Windows
source .venv/bin/activate           # Mac/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file from example
cp .env.example .env

# 4. Fill in your credentials in .env

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Start the server
python manage.py runserver
```

---

## 🔑 Key Concepts Learned

- Django ORM and Model definition
- MySQL integration with Django using `mysqlclient`
- Securing `SECRET_KEY`, `DEBUG`, `DB_PASSWORD` using environment variables
- `makemigrations` and `migrate` workflow