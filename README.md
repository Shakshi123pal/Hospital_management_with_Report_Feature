# 🏥 Hospital Management System with Report Feature

This is a FastAPI-based backend for a hospital management system with features like patient CRUD, JWT auth, and PDF report generation.

## 🚀 Live Demo

👉 [Click here to visit the deployed API on Render](https://hospital-management-api-m7j5.onrender.com)

📄 Swagger UI Docs: [https://hospital-management-api-m7j5.onrender.com/docs](https://hospital-management-api-m7j5.onrender.com/docs)

## 📂 Features

- User authentication with JWT
- Patient registration & CRUD
- Report generation (PDF)
- PostgreSQL database
- Deployed on Render

## 🛠️ Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Jinja2
- Uvicorn

## ⚙️ Setup Locally

```bash
git clone https://github.com/Shakshi123pal/Hospital_management_with_Report_Feature.git
cd Hospital_management_with_Report_Feature
pip install -r requirements.txt
uvicorn main:app --reload
