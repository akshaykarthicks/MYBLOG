# MYBLOG - Django Blog Project

A simple blog application built with Django that allows users to create and view blog posts.
https://myblog-xwlx.onrender.com

![Screenshot 2025-05-27 202203](https://github.com/user-attachments/assets/7061892d-80f8-444b-9d0e-3e19d681e419)
![Screenshot 2025-05-27 202209](https://github.com/user-attachments/assets/2defdaf6-86a1-4ba3-8568-68fcaff9820f)
![Screenshot 2025-05-27 202217](https://github.com/user-attachments/assets/b20cb4f6-8623-4356-a49e-a2f2b2fd4b37)





## Project Structure

```
blog/
├── manage.py              # Django's command-line utility
├── blog/                  # Main project directory
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py           # Main URL routing
│   ├── asgi.py           # ASGI configuration
│   └── wsgi.py           # WSGI configuration
│
├── post/                  # Blog post application
│   ├── __init__.py
│   ├── models.py         # Blog post model
│   ├── views.py          # View logic for posts
│   ├── urls.py           # URL patterns for posts
│   ├── admin.py          # Admin configuration
│   └── apps.py           # App configuration
│
├── templates/            # HTML templates
│   ├── index.html       # Home page
│   ├── posts.html       # Posts listing page
│   └── create_post.html # Create new post page
│
└── db.sqlite3           # SQLite database file
```

## Features

- Create new blog posts
- View list of all blog posts
- View individual blog posts
- Admin interface for post management

## Technology Stack

- Python 3.x
- Django 5.0.1
- SQLite Database
- HTML/CSS

## Templates

The project includes three main templates:
- `index.html`: Home page
- `posts.html`: Displays all blog posts
- `create_post.html`: Form for creating new posts

## Admin Interface

The project includes Django's admin interface at `/admin/` where you can:
- Manage blog posts
- Add, edit, or delete posts
