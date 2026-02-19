# Contributing Guidelines

Terima kasih atas ketertarikan Anda untuk berkontribusi pada project ini 
Project ini merupakan bagian dari **Praktikum Big Data – Setup Environment & Spark Workflow** dan terbuka untuk kontribusi yang bersifat edukatif maupun pengembangan fitur tambahan.

---

## Tujuan Kontribusi

Kontribusi dapat berupa:

- Perbaikan bug
- Penyempurnaan dokumentasi
- Penambahan contoh Spark job
- Perbaikan struktur project
- Penambahan integrasi data (MongoDB, CSV, API, dll)
- Optimalisasi konfigurasi environment
- Penambahan best practices untuk Big Data workflow

---

## Struktur Project

```
bigdata-project/
│
├── scripts/            # Spark jobs & MongoDB connection script
├── notebooks/          # Optional exploratory notebook
├── data/               # Sample dataset (jika ada)
├── docs/               # Dokumentasi & screenshots
├── .env                # Environment variables (tidak di-commit)
├── .gitignore
├── README.md
└── CONTRIBUTING.md
```

Harap pertahankan struktur ini saat menambahkan file baru.

---

## Security & Sensitive Information

⚠ **JANGAN PERNAH** meng-commit:

- MongoDB URI
- API Keys
- Password
- File `.env`
- Credential apapun

Gunakan file `.env` untuk menyimpan konfigurasi sensitif:

```
MONGO_URI=your_mongodb_connection_string
```

Pastikan `.env` sudah terdaftar dalam `.gitignore`.

---

## Cara Berkontribusi

### Fork Repository

Klik tombol **Fork** di GitHub.

---

### Clone Repository

```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

---

### Buat Branch Baru

Gunakan nama branch yang deskriptif:

```bash
git checkout -b feature/add-spark-job
```

Contoh branch naming:

- `feature/add-data-cleaning`
- `fix/mongodb-connection`
- `docs/update-readme`
- `refactor/project-structure`

---

### Lakukan Perubahan

Pastikan:

- Kode dapat dijalankan
- Tidak ada hardcoded credentials
- Struktur tetap rapi
- Dokumentasi diperbarui jika perlu

---

### Commit dengan Format yang Jelas

Gunakan conventional commit style:

```bash
git commit -m "feat: add spark aggregation example"
git commit -m "fix: resolve mongodb connection issue"
git commit -m "docs: update installation guide"
```

Format umum:

```
type: short description
```

Type yang digunakan:
- `feat`
- `fix`
- `docs`
- `refactor`
- `chore`

---

### Push & Pull Request

```bash
git push origin feature/add-spark-job
```

Lalu buat **Pull Request** ke branch `main`.

---

## Testing Guidelines

Sebelum membuat Pull Request, pastikan:

- Spark job berjalan tanpa error
- MongoDB connection berhasil (jika relevan)
- Tidak ada dependency yang rusak
- Python version compatible (recommended: Python 3.10)

---

## Code Style Guidelines

- Gunakan Python PEP8 style
- Hindari kode yang terlalu panjang dalam satu file
- Pisahkan logic dan konfigurasi
- Tambahkan komentar pada bagian penting
- Gunakan nama variabel yang deskriptif

Contoh yang baik:

```python
spark = SparkSession.builder.appName("SimpleJob").getOrCreate()
```

Hindari:

```python
x = SparkSession.builder.appName("x").getOrCreate()
```

---

## Environment Requirement

Rekomendasi environment:

- Python 3.10.x
- Java 17
- Apache Spark 4.x
- MongoDB Atlas (Free Tier)
- VS Code

Jika menambahkan dependency baru, update file:

```
requirements.txt
```

---

## Reporting Issues

Jika menemukan bug:

1. Gunakan tab **Issues**
2. Sertakan:
   - Error message lengkap
   - Screenshot (jika ada)
   - Python & Spark version
   - Langkah reproduksi

Format laporan:

```
### Expected behavior
...

### Actual behavior
...

### Steps to reproduce
1.
2.
3.
```

---

## Contribution Philosophy

Project ini dibuat untuk:

- Edukasi Big Data Workflow
- Simulasi arsitektur industri
- Latihan Git & kolaborasi

Kami mendorong kontribusi yang:

- Informatif
- Terstruktur
- Aman
- Reproducible

---

## Code of Conduct

Hormati kontributor lain.

- Tidak toxic
- Tidak spam
- Tidak menyertakan credential sensitif
- Gunakan bahasa profesional

---

## ⭐ Final Note

Setiap kontribusi, sekecil apapun, sangat berarti untuk pengembangan ekosistem pembelajaran Big Data.

Terima kasih telah berkontribusi! 🚀
