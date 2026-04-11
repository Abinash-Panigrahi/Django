# P007 — Django Static Files Integration 

## 📌 Project Overview
This module explores how Django manages and serves static assets. Instead of just rendering plain HTML, this project demonstrates how to bring web pages to life by integrating external CSS stylesheets, images, and media files (like videos) using Django's built-in `{% static %}` template tag system.

## 🎯 Key Learning Objectives
* Structuring a global `static/` directory containing dedicated subfolders for CSS, images, and videos.
* Properly configuring `STATIC_URL` and `STATICFILES_DIRS` within `settings.py` so Django knows where to look for assets.
* Injecting static files into HTML templates using the `{% load static %}` tag.
* Linking external `.css` files to style the webpage.
* Embedding local `.mp4` video files directly into the browser using HTML5 tags.

## 👀 Under the Hood: How It Works

**1. Configuring the Project (`settings.py`)**
We have to explicitly tell Django where our static folder lives relative to the base directory:
```python
STATIC_URL = 'static/'
STATIC_DIR = BASE_DIR / 'static'
STATICFILES_DIRS = [STATIC_DIR,]
```

**2. Injecting Assets (`home.html`)**
To use static files, we must load the static library at the very top of our HTML document. Once loaded, we can dynamically generate the correct paths for our CSS and video files:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="{% static 'css/Style.css' %}">
</head>
<body>
    <h1>Avenger End Game</h1>
    <video src="{% static 'vdo/avengers.mp4' %}" controls></video>
</body>
</html>
```

**3. Routing the View (`urls.py`)**
The app-level routing points directly to our static-rendering view:
```python
path('avenger/', views.avenger_view),
```
*Live URL:* `http://127.0.0.1:8000/StaticApp/avenger/`

## 📁 Directory Architecture
```text
P007/
└── StaticProject/
    ├── manage.py
    ├── static/                   ← Main asset directory
    │   ├── css/                  ← Contains Style.css
    │   ├── img/                  
    │   └── vdo/                  ← Local videos (Excluded from version control)
    ├── templates/
    │   └── StaticApp/
    │       └── home.html         ← Renders the static assets
    ├── StaticProject/
    │   ├── settings.py           ← Static variables defined here
    │   └── urls.py               
    └── StaticApp/
        ├── views.py              ← Returns the home.html template
        └── urls.py               
```

> ⚠️ **Important Note on Version Control:** Large media assets (like `avengers.mp4`) are strictly ignored via `.gitignore` to comply with GitHub's file size limits. To run this project locally, you will need to place your own `.mp4` file inside the `static/vdo/` directory.

## 🚀 Execution Guide
To spin up the development server and view the static page:
```bash
cd StaticProject
python manage.py runserver
```
Navigate to `http://127.0.0.1:8000/StaticApp/avenger/` in your preferred web browser.

## 🛠️ Technology Stack
* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3