# 🏥 Hospital Management System API with Patient Report Feature

A robust and scalable Hospital Management backend system built using **FastAPI**. This project provides secure patient and user management with JWT-based authentication, PDF report generation, and RESTful APIs — suitable for integration into a complete hospital software system.



---

##  Key Features
✅ JWT-based Authentication – Secure login and protected APIs.
🧑‍⚕️ Doctor Management – Add, view, update, and delete doctor records.
🧑‍⚕️ Patient Management – Add, view, update, and delete patients with room assignment.
📄 Patient Report Generation – Generate and download patient reports in PDF format.
🗃️ Database Integration – PostgreSQL with SQLAlchemy ORM.
🛡️ Input Validation – Reliable request validation using Pydantic.
🌐 RESTful REST APIs – Modular and scalable API architecture.
☁️ Deployed on Render – Live backend API with Swagger documentation.

---

## 🧰 Tech Stack

| Tool           | Purpose                         |
|----------------|---------------------------------|
| **FastAPI**     | Web framework for building APIs |
| **PostgreSQL**  | Relational database             |
| **SQLAlchemy**  | ORM for database interaction    |
| **Pydantic**    | Data validation and parsing     |
| **Jinja2**      | For rendering dynamic PDF reports |
| **Uvicorn**     | ASGI server for FastAPI         |

## ⚙️ Setup Locally

```bash
git clone https://github.com/Shakshi123pal/Hospital_management_with_Report_Feature.git
cd Hospital_management_with_Report_Feature
pip install -r requirements.txt
uvicorn main:app --reload

💼 Author
Shakshi Pal
MSc Data Science | Aspiring Data Scientist
📫 Connect with me: linkedin.com/in/shakshi-pal-17307926b  
🌐 GitHub: https://github.com/Shakshi123pal


📌 Note
This project is backend-only. You can integrate it with a frontend using React, Vue, or any mobile app framework.
