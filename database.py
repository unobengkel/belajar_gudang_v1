"""
database.py
Modul koneksi dan inisialisasi database SQLite.
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "gudang.db")


def get_connection() -> sqlite3.Connection:
    """Mengembalikan koneksi SQLite dengan row_factory."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    """Membuat tabel-tabel jika belum ada."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS satuan (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS jenis (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS merek (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS barang (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            nama     TEXT    NOT NULL,
            idjenis  INTEGER REFERENCES jenis(id)  ON DELETE SET NULL,
            idsatuan INTEGER REFERENCES satuan(id) ON DELETE SET NULL,
            idmerek  INTEGER REFERENCES merek(id)  ON DELETE SET NULL
        );

        CREATE TABLE IF NOT EXISTS stok (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            idbarang INTEGER NOT NULL REFERENCES barang(id) ON DELETE CASCADE,
            jumlah   REAL    NOT NULL DEFAULT 0,
            datetime TEXT    NOT NULL
        );
    """)

    conn.commit()
    conn.close()
    print("[DB] Database initialized.")
