 

![banner](banner.png)  

#  Library Management System

Welcome to the **Library Management System** — a full-stack Django web application that lets users browse, borrow, and return books, while an admin can manage the library (add, delete books), and view users’ borrow history. You can try the live version here:

[Live Demo](https://library-management-system-jewe.onrender.com/)  

---

##  Table of Contents

1. [Features](#features)  
2. [Screenshots](#screenshots)  
3. [Tech Stack](#tech-stack)  
4. [Getting Started](#getting-started)  
5. [Usage](#usage)  
6. [Permissions & Roles](#permissions--roles)  
7. [Project Structure](#project-structure)  
 

---

##  Features

- **Authentication**: Sign up, login, logout  
- **User Portal**:
  - Browse all books  
  - Search books by title or author  
  - Borrow and return books  
  - View “My Books” (your borrowing history)  
- **Admin Portal**:
  - Add new books (with image, title, author)  
  - Delete books  
  - Mark books as available / unavailable  
- **Responsive UI**: Clean, mobile-friendly design  
- **Media Support**: Upload book cover images  
  

---

##  Screenshots

Add screenshot images in your GitHub repo (for example in `/assets/` or `/docs/`) and reference them here. For example:

![Homepage](home.png)  
*Home page showing list of books*

![Borrow Book](borrowbook.png)  
*Borrow confirmation modal*

 

---

## 🛠 Tech Stack

- **Backend**: Django  
- **Frontend**: HTML,  CSS framework  
- **Database**: PostgreSQL (on Render)  
- **File Storage**: Django Media for book images  
- **Deployment**: Render.com  

---

##  Getting Started

Follow these instructions to run the project locally.

### Prerequisites

- Python 3.8+  
- `pip` installed  
- Virtual environment (recommended)

### Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/sayyedrabeeh/LibraryMS.git
   cd LibraryMS
````

2. **Create and activate virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file (or set in your environment) containing:

   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/dbname
   ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser.

---

##  Usage

* **User Flow**:

  1. Sign up / login
  2. Browse available books
  3. Click *Borrow Book* → confirmation modal
  4. Borrowed books no longer available for others
  5. Go to **My Books** page to view your borrow history and return books

* **Admin Flow**:

  1. Log in to your superuser/admin
  2. Add new books with details + image
  3. Delete existing or manage book availability
  4. View all users’ borrow records

---

##  Permissions & Roles

| Role      | Permissions                                        |
| --------- | -------------------------------------------------- |
| **User**  | Browse, Borrow, Return, View own borrow history    |
| **Admin** | Add / Delete Books, View all users’ borrow records |

This ensures that only an admin (superuser) can perform library management operations like adding or deleting books, while normal users just borrow and return books.

---

##  Project Structure

```
LibraryMS/
├── library_project/        # Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── library_app/            # Core library app
│   ├── models.py          # Book, BorrowRecord models
│   ├── views.py
│   ├── templates/
│   └── static/
├── media/                  # Uploaded book images
├── templates/              # Project-level templates
├── requirements.txt
└── README.md               # <-- This file
```

---



##  Author & Contact

* **Author**: Sayyed Rabeeh
* **GitHub**: [sayyedrabeeh](https://github.com/sayyedrabeeh)
* **Live Site**: [LibraryMS on Render](https://library-management-system-jewe.onrender.com/)

---

##  License

This project is licensed under the MIT License. Feel free to use, modify, and distribute as you like.

---

```

