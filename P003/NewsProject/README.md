# P003 — Multiple Apps with App-Level URL Routing

## 📌 About
This project demonstrates how to create multiple Django apps inside a single project and connect them using both project-level and app-level URL routing.

## 🎯 What This Covers
- Creating multiple Django apps inside one project
- Registering apps in `settings.py`
- Writing function-based views returning `HttpResponse`
- Setting up **app-level** `urls.py` for each app
- Using `include()` in project-level `urls.py` to connect all apps

## 👀 How It Works

**Project-level urls.py** connects each app using `include()`:
```python
path('CricketApp/', include('CricketApp.urls')),
path('EducationApp/', include('EducationApp.urls')),
path('PoliticsApp/', include('PoliticsApp.urls')),
```

**App-level urls.py** maps each URL to its view:
```python
path('education/', views.Education_view),
path('todays_education/', views.Now_a_days_Education_system),
```

Each app has its own views returning `HttpResponse` with HTML content directly.

## 📁 Project Structure
```
P003/
└── NewsProject/
    ├── manage.py
    ├── NewsProject/          ← Project config
    │   ├── settings.py
    │   └── urls.py           ← Connects all 3 apps using include()
    ├── CricketApp/
    │   ├── views.py          ← Cricket related views
    │   └── urls.py           ← App level URLs
    ├── EducationApp/
    │   ├── views.py          ← Education related views
    │   └── urls.py           ← App level URLs
    └── PoliticsApp/
        ├── views.py          ← Politics related views
        └── urls.py           ← App level URLs
```

## 🚀 How to Run
```bash
cd NewsProject
python manage.py runserver
```

Then visit any of these URLs in your browser:
- `http://127.0.0.1:8000/CricketApp/cricket/`
- `http://127.0.0.1:8000/EducationApp/education/`
- `http://127.0.0.1:8000/PoliticsApp/politics/`

## 🛠️ Tech Used
- Python
- Django