# PRAKTIKUM WEEK 1: SETUP ENVIRONMENT & GIT WORKFLOW

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10.11-blue?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/PySpark-Enabled-orange?style=for-the-badge&logo=apachespark&logoColor=white"/>
<img src="https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white"/>
<img src="https://img.shields.io/badge/Java-17-red?style=for-the-badge&logo=openjdk&logoColor=white"/>
<img src="https://img.shields.io/badge/Git-Workflow-F05032?style=for-the-badge&logo=git&logoColor=white"/>

</p>

Praktikum Big Data Technology  
Topik: Setup Environment, PySpark, MongoDB Atlas, dan Git Workflow

## Deskripsi

Praktikum ini merupakan bagian dari mata kuliah **Teknologi Big Data** yang berfokus pada proses setup environment pengembangan serta workflow Git dalam proyek Big Data. Pada praktikum ini, mahasiswa membangun environment dari nol hingga dapat menjalankan Spark job sederhana dan mengintegrasikannya dengan cloud database MongoDB Atlas. Pendekatan yang digunakan mencerminkan workflow industri modern: Local Development → Distributed Processing → Cloud Integration → Version Control

---

## Tim Developer

| Peran | Nama | NIM | Profil GitHub |
| :--- | :--- | :--- | :--- |
| **Pengembang Proyek** | M. Kaspul Anwar | 230104040212 | [![](https://img.shields.io/badge/GitHub-M.KaspulAnwar-181717?style=flat&logo=github)](https://github.com/mkaspulanwar) |
| **Dosen Pengampu** | Muhayat, M. IT | - | [![](https://img.shields.io/badge/GitHub-Muhayat,M.IT-181717?style=flat&logo=github)](https://github.com/muhayat-lab) |

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. Menggunakan VS Code sebagai environment kerja
2. Menjalankan perintah CLI melalui PowerShell / Terminal
3. Menginstal dan menjalankan PySpark di Windows
4. Membuat dan menghubungkan MongoDB Atlas (cloud database)
5. Membuat struktur project Python yang rapi dan profesional
6. Menggunakan Git dan GitHub dalam workflow development
7. Menjalankan Spark job sederhana untuk agregasi data

---

## Tech Stack

- Python 3.10.x
- PySpark
- MongoDB Atlas (M0 Free Tier)
- pymongo
- python-dotenv

---

## Struktur Folder Project

```
bigdata-project/
│
├── data/
├── cloud_storage/
├── notebooks/
├── reports/
│
├── scripts/
│   ├── simple_job.py
│   └── test_mongo.py
│
├── requirements.txt
├── .env              # (tidak di-commit)
├── .gitignore
└── README.md
```

---

## Setup Environment

### Install Python

Gunakan Python **3.10.11**  
(PySpark lebih stabil di 3.10 dibanding 3.14)

Cek versi:
```
python --version
```

---

### Install Dependencies

Di root project:

```
pip install pyspark pymongo python-dotenv
```

Atau gunakan `requirements.txt`:

```
pip install -r requirements.txt
```

Contoh isi `requirements.txt`:

```
pyspark
pymongo
python-dotenv
```

---

## Menjalankan Spark Job

File: `scripts/simple_job.py`

Jalankan:

```
python scripts/simple_job.py
```

Expected output:

```
+--------+----------+
|category|sum(value)|
+--------+----------+
|       A|        40|
|       B|        20|
+--------+----------+
```

Jika muncul warning `winutils.exe`, itu normal di Windows dan bisa diabaikan.

---

## Troubleshooting PySpark di Windows

Jika muncul error:

```
Cannot run program "python3"
```

Itu karena Spark mencari `python3` (Linux style), sedangkan di Windows biasanya hanya ada `python`.

Solusi sementara di PowerShell:

```
$env:PYSPARK_PYTHON="C:\Users\<username>\AppData\Local\Programs\Python\Python310\python.exe"
$env:PYSPARK_DRIVER_PYTHON="C:\Users\<username>\AppData\Local\Programs\Python\Python310\python.exe"
```

Atau jalankan dengan spark-submit:

```
spark-submit --conf spark.pyspark.python=PATH_PYTHON `
             --conf spark.pyspark.driver.python=PATH_PYTHON `
             scripts/simple_job.py
```

---

## Setup MongoDB Atlas

Langkah umum:

1. Login ke MongoDB Atlas
2. Buat Cluster (M0 Free Tier)
3. Buat Database User
4. Whitelist IP Address
5. Ambil Connection String (Driver: Python)

---

## Keamanan: Gunakan .env untuk Mongo URI

⚠ Jangan simpan URI MongoDB langsung di file Python jika project akan di-push ke GitHub.

---

### Buat file `.env` (di root project)

```
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
```

---

### Tambahkan `.env` ke `.gitignore`

Buat file `.gitignore`:

```
# Python
__pycache__/
*.pyc
.venv/

# Secrets
.env
```

---

### Update `test_mongo.py`

Gunakan dotenv agar credential aman:

```python
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGODB_URI")

if not uri:
    raise ValueError("MONGODB_URI belum diset. Buat file .env terlebih dahulu.")

try:
    client = MongoClient(uri)
    print("Koneksi berhasil!")
    print(client.list_database_names())
except Exception as e:
    print("Koneksi gagal:", e)
```

Jalankan:

```
python scripts/test_mongo.py
```

---

## Git Workflow

Inisialisasi repository:

```
git init
git add .
git commit -m "Initial project setup"
git branch -M main
git remote add origin <URL_REPO>
git push -u origin main
```

---

## ⚠️ Catatan Keamanan

Jika URI MongoDB pernah di-commit:

1. Hapus dari file Python
2. Pindahkan ke `.env`
3. Tambahkan `.env` ke `.gitignore`
4. Regenerate password MongoDB Atlas

---
