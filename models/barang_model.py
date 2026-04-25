"""models/barang_model.py — SQL model mapping untuk Barang"""
from database import get_connection
from entities.barang import Barang
from typing import List, Optional


_JOIN_SQL = """
    SELECT b.id, b.nama, b.idjenis, b.idsatuan, b.idmerek,
           j.nama AS nama_jenis,
           s.nama AS nama_satuan,
           m.nama AS nama_merek
    FROM barang b
    LEFT JOIN jenis   j ON j.id = b.idjenis
    LEFT JOIN satuan  s ON s.id = b.idsatuan
    LEFT JOIN merek   m ON m.id = b.idmerek
"""


class BarangModel:
    @staticmethod
    def row_to_entity(row) -> Barang:
        return Barang(
            id=row["id"],
            nama=row["nama"],
            idjenis=row["idjenis"],
            idsatuan=row["idsatuan"],
            idmerek=row["idmerek"],
            nama_jenis=row["nama_jenis"],
            nama_satuan=row["nama_satuan"],
            nama_merek=row["nama_merek"],
        )

    @staticmethod
    def find_all() -> List[Barang]:
        conn = get_connection()
        rows = conn.execute(_JOIN_SQL + " ORDER BY b.nama").fetchall()
        conn.close()
        return [BarangModel.row_to_entity(r) for r in rows]

    @staticmethod
    def find_by_id(id_: int) -> Optional[Barang]:
        conn = get_connection()
        row = conn.execute(_JOIN_SQL + " WHERE b.id = ?", (id_,)).fetchone()
        conn.close()
        return BarangModel.row_to_entity(row) if row else None

    @staticmethod
    def insert(nama: str, idjenis, idsatuan, idmerek) -> int:
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO barang (nama, idjenis, idsatuan, idmerek) VALUES (?,?,?,?)",
            (nama, idjenis, idsatuan, idmerek),
        )
        conn.commit()
        last_id = cur.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def update(id_: int, nama: str, idjenis, idsatuan, idmerek) -> bool:
        conn = get_connection()
        cur = conn.execute(
            "UPDATE barang SET nama=?, idjenis=?, idsatuan=?, idmerek=? WHERE id=?",
            (nama, idjenis, idsatuan, idmerek, id_),
        )
        conn.commit()
        affected = cur.rowcount
        conn.close()
        return affected > 0

    @staticmethod
    def delete(id_: int) -> bool:
        conn = get_connection()
        cur = conn.execute("DELETE FROM barang WHERE id = ?", (id_,))
        conn.commit()
        affected = cur.rowcount
        conn.close()
        return affected > 0
