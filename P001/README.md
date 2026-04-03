# P001 — First Django Project Setup

## 📌 About
This is the very first Django project — focused purely on understanding how Django works by setting up a project from scratch using the command line.

## 🎯 What This Covers
- Installing Django
- Creating a new Django project using `django-admin startproject`
- Understanding the auto-generated project structure and what each file does
- Running the Django development server for the first time

## 📁 Project Structure
```
P001/
└── MsgProject/
    ├── manage.py            ← Entry point to run the project
    ├── MsgProject/          ← Project configuration folder
    │   ├── settings.py      ← All project settings live here
    │   ├── urls.py          ← URL declarations
    │   ├── asgi.py          ← ASGI configuration
    │   └── wsgi.py          ← WSGI configuration
    └── MsgApp/              ← First auto-created app folder
```

## 🚀 How to Run
```bash
cd MsgProject
python manage.py runserver
```

Then open `http://127.0.0.1:8000` in your browser.

## 🛠️ Tech Used
- Python
- Django