# 🏥 Hospital Management Backend App with FastAPI

This is a backend-only Hospital Management System built using **FastAPI**, **SQLite3**, and **OAuth 2.0**. The application allows admin-authenticated operations for managing doctors and patients with a many-to-many relationship.

🔗 Live Render Link: _Coming Soon_  
👤 Developed by: **Shakshi**, MSc Data Science Student  

---

## 🚀 Overview

This project simulates a real-world hospital management backend system. Admins can:
- Add/Edit/Delete doctors
- Add/Edit/Delete patients
- Assign doctors to patients
- Authenticate using OAuth2

> ⚠️ This is a backend-only application. Use `/docs` (Swagger UI) or Postman for testing endpoints.

---

## 🛠️ Tech Stack

- **FastAPI** – for building RESTful APIs
- **SQLite** – as the database
- **SQLAlchemy** – for ORM
- **OAuth2.0 + JWT** – for secure admin authentication
- **Uvicorn** – as ASGI server

---

## 📦 Installation

```bash
# 1. Clone this repository
git clone https://github.com/Shakshi123pal/Hospital_management__with_Report_Feature.git

# 2. Navigate into the project folder
cd hospital-management-fastapi

# 3. Install dependencies
pip install -r req.txt

# 4. Run the app locally
uvicorn main:app --reload
