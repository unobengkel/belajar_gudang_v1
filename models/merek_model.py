"""models/merek_model.py — SQL model mapping untuk Merek"""
from database import get_connection
from entities.merek import Merek
from typing import List, Optional


class MerekModel:
    @staticmethod
    def row_to_entity(row) -> Merek:
        return Merek(id=row["id"], nama=row["nama"])

    @staticmethod
    def find_all() -> List[Merek]:
        conn = get_connection()
        rows = conn.execute("SELECT * FROM merek ORDER BY nama").fetchall()
        conn.close()
        return [MerekModel.row_to_entity(r) for r in rows]

    @staticmethod
    def find_by_id(id_: int) -> Optional[Merek]:
        conn = get_connection()
        row = conn.execute("SELECT * FROM merek WHERE id = ?", (id_,)).fetchone()
        conn.close()
        return MerekModel.row_to_entity(row) if row else None

    @staticmethod
    def insert(nama: str) -> int:
        conn = get_connection()
        cur = conn.execute("INSERT INTO merek (nama) VALUES (?)", (nama,))
        conn.commit()
        last_id = cur.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def update(id_: int, nama: str) -> bool:
        conn = get_connection()
        cur = conn.execute("UPDATE merek SET nama = ? WHERE id = ?", (nama, id_))
        conn.commit()
        affected = cur.rowcount
        conn.close()
        return affected > 0

    @staticmethod
    def delete(id_: int) -> bool:
        conn = get_connection()
        cur = conn.execute("DELETE FROM merek WHERE id = ?", (id_,))
        conn.commit()
        affected = cur.rowcount
        conn.close()
        return affected > 0
