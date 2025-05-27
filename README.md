# 🚍 Big Data Pipeline untuk Analisis Penumpang TransJakarta

Proyek ini bertujuan membangun pipeline big data berbasis ekosistem Hadoop untuk mengelola data penumpang TransJakarta secara batch processing menggunakan pendekatan arsitektur Medallion (Bronze, Silver, Gold). Analisis dilakukan untuk mendukung pengambilan keputusan operasional berbasis data.

---

## 🧑‍🤝‍🧑 Tim Kelompok 15  
- Ramadhita Atifa Hendri (121450131)  
- Oktavia Nurwinda Puspitasari (122450041)  
- Nasywa Nur Afifah (122450125)  
- Muhammad Zaky Zaiddan (122450119)  

---

## 🏗️ Arsitektur Sistem

| Layer             | Teknologi          | Fungsi                                               |
|-------------------|--------------------|------------------------------------------------------|
| **Storage Layer** | HDFS               | Menyimpan data mentah dan hasil transformasi         |
| **Metadata SQL**  | Hive               | Query data dengan bahasa SQL                         |
| **Batch Engine**  | Apache Spark       | Pembersihan & transformasi data                      |
| **NoSQL Storage** | HBase              | Penyimpanan data detail yang cepat diakses           |
| **Container**     | Docker             | Reproduksi lingkungan kerja                          |

---

## 🔄 Alur Proyek

1. **Bronze Layer:** Menyimpan data mentah (CSV → Parquet)
2. **Silver Layer:** Membersihkan & mentransformasi data (validasi, durasi)
3. **Gold Layer:** Menghitung rata-rata durasi perjalanan per koridor
4. **Visualisasi:** Menggunakan Python (Matplotlib, Seaborn)
5. **Deploy lokal:** Menggunakan Docker dengan cluster Hadoop

---

## 🧱 Metode Penelitian

Menggunakan metode **Waterfall**, dimulai dari:
- Analisis kebutuhan
- Perancangan arsitektur Medallion
- Implementasi pipeline
- Validasi dan pengujian sistem
- Visualisasi dan analisis data

---

## 📁 Struktur Folder (Rekomendasi)

- 📦 `docker/` → File Dockerfile, build.sh, bootstrap.sh
- 🛠️ `hadoop-config/` → File konfigurasi Hadoop (XML, SH)
- 📊 `data/` → Dataset penumpang TransJakarta
- 🧪 `scripts/` → Script Python atau Spark
- 🖼️ `images/` → Gambar visualisasi atau arsitektur
- 📘 `README.md` → Penjelasan proyek
- 🚫 `.gitignore` → File untuk mengabaikan file tertentu

---

## ▶️ Cara Menjalankan Project

1. **Clone Repository**
   ```bash
   git clone https://github.com/username/repo-ini.git
   cd repo-ini
