# StudyCase1
# 🤖 Study Case 1 ROBOTIIK

## 📌 Deskripsi Proyek
Proyek ini merupakan implementasi **Object-Oriented Programming (OOP)** dalam Python yang mensimulasikan **sistem kontrol rumah pintar (Smart Home System)**. Program ini menggunakan library `keyboard` untuk mendeteksi input dari pengguna dalam bentuk penekanan tombol, dan menjalankan logika kendali perangkat pintar rumah seperti **lampu otomatis**, **kipas**, dan **sensor suhu**.

Proyek ini dibuat sebagai bagian dari **Studi Kasus 1 mata kuliah ROBOTIIK**.

---

## ⚙️ Fitur Program

- ✅ Menggunakan konsep **OOP** (class, objek, enkapsulasi)
- ✅ Menggunakan **multi-threading** agar tiap perangkat dapat berjalan secara paralel
- ✅ Tombol dapat digunakan untuk **menghidupkan dan mematikan** perangkat secara **toggle**
- ✅ Menampilkan status rumah saat semua perangkat aktif
- ✅ Simulasi realistis kontrol perangkat dalam smart home

---

## 🧠 Komponen Utama

| Perangkat       | Tombol | Fungsi                             |
|----------------|--------|------------------------------------|
| Lampu Otomatis | `l`    | Nyalakan/matikan lampu             |
| Kipas Otomatis | `k`    | Nyalakan/matikan kipas             |
| Sensor Suhu    | `t`    | Nyalakan/matikan sensor suhu       |

---

## 🖥️ Cara Menjalankan Program

### 1. Install Library
Program membutuhkan library `keyboard`. Jalankan perintah berikut di terminal:
```bash
pip install keyboard
