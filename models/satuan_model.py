"""models/satuan_model.py — SQL model mapping untuk Satuan"""
from database import get_connection
from entities.satuan import Satuan
from typing import List, Optional


class SatuanModel:
    TABLE = "satuan"

    @staticmethod
    def row_to_entity(row) -> Satuan:
        return Satuan(id=row["id"], nama=row["nama"])

    @staticmethod
    def find_all() -> List[Satuan]:
        conn = get_connection()
        rows = conn.execute(f"SELECT * FROM satuan ORDER BY nama").fetchall()
        conn.close()
        return [SatuanModel.row_to_entity(r) for r in rows]

    @staticmethod
    def find_by_id(id_: int) -> Optional[Satuan]:
        conn = get_connection()
        row = conn.execute("SELECT * FROM satuan WHERE id = ?", (id_,)).fetchone()
        conn.close()
        return SatuanModel.row_to_entity(row) if row else None

    @staticmethod
    def insert(nama: str) -> int:
        conn = get_connection()
        cur = conn.execute("INSERT INTO satuan (nama) VALUES (?)", (nama,))
        conn.commit()
        last_id = cur.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def update(id_: int, nama: str) -> bool:
        conn = get_connection()
        cur = conn.execute("UPDATE satuan SET nama = ? WHERE id = ?", (nama, id_))
        conn.commit()
        affected = cur.rowcount
        conn.close()
        return affected > 0

    @staticmethod
    def delete(id_: int) -> bool:
        conn = get_connection()
        cur = conn.execute("DELETE FROM satuan WHERE id = ?", (id_,))
        conn.commit()
        affected = cur.rowcount
        conn.close()
        return affected > 0
