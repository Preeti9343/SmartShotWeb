# 📸 SmartShotWeb  
### AI-Powered Screenshot Extraction & Text Search (Django Web Application)

SmartShotWeb is a **Django-based web application** designed to extract text from screenshots, store metadata, display extracted content, and generate CSV reports.  
It allows users to upload images and instantly get OCR-extracted text using Tesseract/PyTesseract with a clean Django interface.

---

## ✨ Key Features

### 🔍 **1. OCR Text Extraction**
- Extracts text from PNG/JPG screenshots  
- Uses **PyTesseract** for OCR  
- Handles noisy screenshots with custom preprocessing

### 📝 **2. CSV Export**
- Saves extracted text to `extracted_text.csv`  
- Supports bulk export  
- Ideal for analysis or dataset creation

### 🗂️ **3. Screenshot Management**
- Upload screenshots  
- Store details using Django Models  
- Track file name, upload time, and extracted text  
- Organised storage inside `screenshots/` folder

### ⚡ **4. Django Admin Panel**
- View, edit, delete screenshot entries  
- Search inside extracted text  
- Manage records easily for debugging/testing

### 🧠 **5. Utilities Included**
- `generate_csv.py` – exports all DB entries  
- `utils.py` – helper functions for image handling

---

## 🧱 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.10+** | Backend development |
| **Django** | Web application framework |
| **PyTesseract** | OCR text extraction |
| **SQLite (db.sqlite3)** | Local database |
| **HTML + Django Templates** | Frontend UI |
| **Pillow** | Image processing |

---

## 📂 Folder Structure

SmartShotWeb/
├── screenshots/ # Uploaded images

│ ├── migrations/

│ ├── templates/ # HTML templates

│ ├── apps.py

│ ├── models.py # Screenshot model

│ ├── utils.py # Helper utilities

│ ├── views.py # Core logic

│ ├── urls.py

│ └── tests.py
│
├── SmartShotWeb/

│ ├── settings.py

│ ├── urls.py

│ └── wsgi.py

│
├── static/ # Static assets

├── extracted_text.csv # Exported text file

├── generate_csv.py # CSV script

├── db.sqlite3 # Database

├── manage.py

└── venv/ # Virtual environment  


---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Preeti9343/SmartShotWeb.git
cd SmartShotWeb

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate    # Windows

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py migrate

5️⃣ Run the Server
python manage.py runserver
