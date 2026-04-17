# P009 — Displaying Database Records in HTML Template

## 📌 What This Project Covers
- Fetching all records from a MySQL database using Django ORM (`objects.all()`)
- Passing retrieved records to an HTML template via context dictionary
- Displaying records dynamically in an HTML table using Django template `{% for %}` loop
- App-level URL routing using `include()`

---

## 🗂️ Project Structure

```
P009/
└── DisplayRecords/
    ├── DisplayRecordsApp/
    │   ├── models.py        # Shirt model definition
    │   ├── views.py         # retrieve_view — fetches and sends records to template
    │   ├── urls.py          # App-level URL routing
    │   ├── admin.py         # Default admin file (unused)
    │   └── ...
    ├── DisplayRecords/
    │   ├── settings.py      # Project settings (uses .env)
    │   ├── urls.py          # Includes DisplayRecordsApp URLs
    │   └── ...
    ├── templates/
    │   └── DisplayRecordsApp/
    │       └── shirts.html  # Displays all shirt records in a table
    ├── .env                 # Secret credentials (NOT pushed to GitHub)
    ├── .env.example         # Template for environment variables
    └── manage.py
```

---

## 🧩 Model Used

```python
from django.db import models

class Shirt(models.Model):
    brand = models.CharField(max_length=20)
    price = models.FloatField()
    color = models.CharField(max_length=20)
```

---

## 👁️ View

```python
from django.shortcuts import render
from .models import Shirt

def retrieve_view(request):
    record = Shirt.objects.all()
    d = {'records': record}
    return render(request, 'DisplayRecordsApp/shirts.html', d)
```

---

## 🔗 URL Configuration

**Project level (`DisplayRecords/urls.py`)**
```python
path('DisplayRecordsApp/', include('DisplayRecordsApp.urls'))
```

**App level (`DisplayRecordsApp/urls.py`)**
```python
path('Shirt/', views.retrieve_view)
```

**Access at:** `http://127.0.0.1:8000/DisplayRecordsApp/Shirt/`

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

## 🚀 How to Run Locally

```bash
# 1. Activate virtual environment
.venv\Scripts\activate              # Windows
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

**Then visit:** `http://127.0.0.1:8000/DisplayRecordsApp/Shirt/`

---

## 🔑 Key Concepts Learned

- Django ORM query — `Model.objects.all()`
- Passing queryset to template via context dictionary
- Rendering dynamic data in HTML using `{% for %}` loop
- App-level URL routing with `include()`
- Django template language basics