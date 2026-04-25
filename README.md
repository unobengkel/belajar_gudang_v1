# Gudang V1 - Warehouse Management System

Sistem manajemen stok gudang sederhana yang dibangun dengan Python, SQLite, dan Tailwind CSS. Project ini mengimplementasikan **Clean Architecture** untuk memastikan kode terstruktur, mudah dipelihara, dan dapat dikembangkan.

## 🚀 Fitur Utama

- **Dashboard Real-time**: Ringkasan jumlah master data dan total stok per barang.
- **Master Data**: Kelola data Jenis Barang, Satuan, Merek, dan Barang.
- **Manajemen Stok**: Pencatatan transaksi stok masuk/keluar secara detail.
- **Search Global**: Pencarian data cepat di setiap tabel.
- **Responsive UI**: Desain modern menggunakan Tailwind CSS dengan skema warna yang premium.
- **Clean Architecture**: Terbagi menjadi layer Entity, DTO, Model, Repository, Service, dan Route.

## 🛠️ Tech Stack

- **Backend**: Python (Built-in `http.server`)
- **Database**: SQLite3
- **Templating**: Jinja2
- **Frontend**: Tailwind CSS (via CDN)
- **Icons**: Inline Heroicons & Lucide style

## 📁 Struktur Folder

```text
gudang_v1/
├── main.py              # Entry point & Router
├── database.py          # Konfigurasi SQLite
├── requirements.txt     # Dependensi (Jinja2)
├── entities/            # Objek Domain
├── dto/                 # Data Transfer Objects (Validasi)
├── models/              # Akses Database (SQL)
├── repositories/        # Abstraksi Data
├── services/            # Logika Bisnis
├── routes/              # Handler HTTP & Rendering
└── templates/           # Layout & Halaman HTML
```

## ⚙️ Instalasi

1. **Clone project** ke direktori lokal Anda.
2. **Install dependensi**:
   ```powershell
   pip install -r requirements.txt
   ```
3. **Jalankan aplikasi**:
   ```powershell
   python main.py
   ```
4. **Buka browser** dan akses: `http://localhost:8080`

## 📸 Screenshots

### Dashboard
![Dashboard](assets/dashboard.png)

### Manajemen Stok
![Stok Gudang](assets/stok.png)

## 📝 Lisensi
Distribusi bebas untuk tujuan pembelajaran.
