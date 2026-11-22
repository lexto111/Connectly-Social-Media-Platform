# Connectly – Social Media Platform

A modern social media platform built using Python and Django, where users can connect, share posts, interact with others and build their online community.

## 🚀 Features

- User Registration and Login
- User Profiles
- Edit Profile – Bio, Location and Profile Picture
- Create Posts with Images and Captions
- Like and Unlike Posts
- Comment on Posts
- Follow and Unfollow Users
- Followers and Following Lists
- Explore Users
- Search Users by Username

## 🛠️ Technologies Used

**Frontend**
- HTML
- CSS
- JavaScript

**Backend**
- Python
- Django

**Database**
- SQLite

**Tools**
- VS Code
- Git
- GitHub

## 📂 Project Structure

```text
Connectly/
│
├── connectly/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── network/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── social/
│
├── manage.py
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/lexto111/Connectly-Social-Media-Platform.git
```

### 2. Navigate to the project folder

```bash
cd Connectly-Social-Media-Platform
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```powershell
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install Django==6.1.2 Pillow python-dotenv
```

### 6. Configure environment variables

Create a `.env` file in the project root:

```text
SECRET_KEY=your_generated_secret_key
```

Use your own secret key. Never upload your `.env` file to GitHub.

### 7. Apply database migrations

```bash
python manage.py migrate
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open your browser:

http://127.0.0.1:8000/

## 🎯 Project Goal

The goal of Connectly is to develop a social networking application that allows users to communicate, share content and interact through a simple and user-friendly interface.

## 👨‍💻 Developer

**GitHub:** [lexto111](https://github.com/lexto111)

**Project:** [Connectly Social Media Platform](https://github.com/lexto111/Connectly-Social-Media-Platform)