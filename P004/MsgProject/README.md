# P004 — Personalized Greeting View

## 📌 About
This project practices connecting a Django app to the project using app-level URL routing and returning a personalized greeting message via `HttpResponse`.

## 🎯 What This Covers
- Creating a Django app and registering it in `settings.py`
- Writing a function-based view returning a custom greeting message
- Setting up **app-level** `urls.py`
- Connecting app URLs to project URLs using `include()`

## 👀 How It Works
```python
def Wish_view(request):
    return HttpResponse('Hello Abinash Good morning ; have a nice day ;) ')
```
When the user visits the URL, Django calls `Wish_view()` which returns a plain text greeting as an HTTP response.

**Project-level urls.py:**
```python
path('MsgApp/', include('MsgApp.urls')),
```

**App-level urls.py:**
```python
path('msg/', views.Wish_view),
```

So the full URL is → `http://127.0.0.1:8000/MsgApp/msg/`

## 📁 Project Structure
```
P004/
└── MsgProject/
    ├── manage.py
    ├── MsgProject/          ← Project config
    │   ├── settings.py
    │   └── urls.py          ← Connects MsgApp using include()
    └── MsgApp/
        ├── views.py         ← Wish_view() lives here
        └── urls.py          ← App level URL mapping
```

## 🚀 How to Run
```bash
cd MsgProject
python manage.py runserver
```

Then open `http://127.0.0.1:8000/MsgApp/msg/` in your browser.

## 🛠️ Tech Used
- Python
- Django