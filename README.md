# Analytics API (Django)

A Django-based backend service for uploading CSV files, processing analytics, viewing upload history, and generating PDF analysis reports.

---

## 🚀 Features
- CSV file upload
- Upload history tracking
- PDF report generation
- Django REST-style API endpoints
- Authenticated API access using HTTP Basic Authentication
- Admin support via Django superuser

---

## 🛠 Tech Stack
- Python 3
- Django
- SQLite (default, can be replaced)
- REST-style APIs
- CSV processing & PDF analysis report generation

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/arunimasingh26/analytics-api-django.git
cd analytics-api-django
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄 Database Setup (Migrations)

Run the following commands to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Create a Django user (superuser recommended for admin access)

This project uses **Basic Authentication** with Django users.

Create your own superuser using:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username and password.

> ⚠️ User/Superuser credentials are **not included** in this repository.
> Each user must create their own credentials.

---

## ▶️ Run the Server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## 🔐 API Endpoints

All API endpoints require **Basic Authentication** using Django user credentials.

---

### 1️⃣ Upload CSV File

**Endpoint**

```
POST /api/upload/
```

**Example**

```bash
curl -u <username>:<password> -X POST \
-F file=@sample_equipment_data.csv \
http://127.0.0.1:8000/api/upload/
```

---

### 2️⃣ View Upload History

**Endpoint**

```
GET /api/history/
```

**Example**

```bash
curl -u <username>:<password> \
http://127.0.0.1:8000/api/history/
```

---

### 3️⃣ Generate PDF Report

**Endpoint**

```
GET /api/report/<id>/
```

**Example**

```bash
curl --fail -u <username>:<password> \
http://127.0.0.1:8000/api/report/1/ \
--output report.pdf
```
**Note:** If an invalid dataset ID is provided, the API returns `404 Not Found`. Use `--fail` with `curl` to avoid saving error responses as files.

---

## 📁 Sample Data

A sample CSV file is provided in:

```
analytics/data/sample_equipment_data.csv
```

This can be used to test the upload API.

---

## 🧪 Testing

You can run Django tests using:

```bash
python manage.py test
```

---

## 📌 Notes

* `media/` and `db.sqlite3` are intentionally excluded from version control.
* SQLite is used for simplicity; production deployments should use PostgreSQL or similar.

---

## 📄 License

This project is for educational and demonstration purposes.
