# Book Tracker

A Django web application for managing a personal reading list.

The application allows users to add books, update their reading status, edit book information, delete books, search by title or author, and filter books by reading status.

## Features

- Add new books
- View all books
- Edit existing books
- Delete books
- Track reading status:
  - To Read
  - Reading
  - Read
- Add optional ratings
- Add personal notes
- Search books by title
- Search books by author
- Filter books by status
- Combine search and status filtering
- Django Admin support
- PostgreSQL database
- Responsive basic interface

## Technologies

- Python
- Django
- PostgreSQL
- HTML
- CSS
- python-dotenv
- psycopg2-binary

## Project Structure

```text
book_tracker/
├── book_tracker/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── books/
│   ├── migrations/
│   ├── static/
│   │   └── books/
│   │       └── style.css
│   ├── templates/
│   │   └── books/
│   │       ├── book_list.html
│   │       ├── create_book.html
│   │       ├── edit_book.html
│   │       └── delete_book.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   └── base.html
│
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Book Model

Each book contains:

```text
title
author
genre
status
rating
notes
created_at
```

The available reading statuses are:

```text
To Read
Reading
Read
```

## CRUD Functionality

The project implements full CRUD functionality.

### Create

Users can add a new book through a Django `CreateView`.

### Read

Books are displayed using a Django `ListView`.

### Update

Existing books can be edited using an `UpdateView`.

### Delete

Books can be deleted using a `DeleteView` with a confirmation page.

## Search

Books can be searched by title or author.

The search functionality uses Django `Q` objects:

```python
Q(title__icontains=search) |
Q(author__icontains=search)
```

This allows searching across multiple fields using an OR condition.

## Filtering

Books can also be filtered by reading status:

```text
All statuses
To Read
Reading
Read
```

Search and status filtering can be used together.

Example:

```text
/books/?search=harry&status=reading
```

## PostgreSQL

The application uses PostgreSQL instead of Django's default SQLite database.

Database credentials are stored in a `.env` file and loaded using `python-dotenv`.

Example:

```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

The `.env` file should never be committed to GitHub.

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd book_tracker
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a PostgreSQL database.

Then create a `.env` file with your database configuration.

Run migrations:

```bash
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://localhost:8000/
```

The root URL redirects automatically to the book list.

## Django Admin

The Django Admin panel is available at:

```text
http://localhost:8000/admin/
```

Books can also be managed directly through the admin interface.

## Key Concepts Practiced

This project demonstrates:

- Django project and app structure
- Django models
- PostgreSQL integration
- Environment variables
- Migrations
- Django Admin
- `ModelForm`
- Class-based views
- `ListView`
- `CreateView`
- `UpdateView`
- `DeleteView`
- URL routing
- Templates
- Template inheritance
- Static files
- Search with `Q`
- QuerySet filtering
- GET parameters
- CRUD operations
- Basic frontend styling

## Future Improvements

Possible future improvements include:

- User authentication
- Separate book lists for each user
- Pagination
- Genre filtering
- Sorting
- Book cover images
- Reading statistics
- Improved responsive design