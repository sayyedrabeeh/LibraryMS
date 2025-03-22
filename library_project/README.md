# Library Management System

A Python Django-based library management system that allows users to browse, borrow, and return books. Staff members can manage the library inventory.

## Technologies Used

- **Backend**: Python 3.x, Django 4.x
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production-ready)

## Features

- User authentication (login/signup)
- Book browsing and searching
- Book borrowing and returning system
- Staff-only book management (add/delete books)
- Library statistics and reporting
- CSV export functionality

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
library_management_system/
├── library_app/         # Main application
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── forms.py         # Form validation
│   ├── services.py      # Business logic
│   ├── utils.py         # Utility functions
│   └── templates/       # HTML templates
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## Python Models

The system uses the following models:

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    
class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
```

## License

MIT