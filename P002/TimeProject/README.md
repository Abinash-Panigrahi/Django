# P002 — Displaying Current Time Using Django View

## 📌 About
This project demonstrates how to create a simple Django view that returns a response directly from the server — displaying the current date and time on the browser.

## 🎯 What This Covers
- Creating a Django app
- Writing a function-based view
- Returning an `HttpResponse` directly from a view
- Using Python's `datetime` module inside Django
- Connecting view to URL at the **project level** (no app-level urls.py)

## 👀 How It Works
```python
from django.shortcuts import render, HttpResponse
from datetime import datetime

def get_time(request):
    now = datetime.now()
    return HttpResponse(now)
```
When the user visits the URL, Django calls `get_time()` which fetches the current date and time and returns it directly as an HTTP response in the browser.

## 📁 Project Structure
```
P002/
└── TimeProject/
    ├── manage.py
    ├── TimeProject/       ← Project config — URLs defined here directly
    │   ├── settings.py
    │   ├── urls.py        ← View connected here at project level
    │   ├── asgi.py
    │   └── wsgi.py
    └── TimeApp/
        └── views.py       ← get_time() function lives here
```

## 🚀 How to Run
```bash
cd TimeProject
python manage.py runserver
```

Then open `http://127.0.0.1:8000` in your browser to see the current time.

## 🛠️ Tech Used
- Python
- Django
- Python `datetime` module