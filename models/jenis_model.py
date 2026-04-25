"""models/jenis_model.py — SQL model mapping untuk Jenis"""
from database import get_connection
from entities.jenis import Jenis
from typing import List, Optional


class JenisModel:
    @staticmethod
    def row_to_entity(row) -> Jenis:
        return Jenis(id=row["id"], nama=row["nama"])

    @staticmethod
    def find_all() -> List[Jenis]:
        conn = get_connection()
        rows = conn.execute("SELECT * FROM jenis ORDER BY nama").fetchall()
        conn.close()
        return [JenisModel.row_to_entity(r) for r in rows]

    @staticmethod
    def find_by_id(id_: int) -> Optional[Jenis]:
        conn = get_connection()
        row = conn.execute("SELECT * FROM jenis WHERE id = ?", (id_,)).fetchone()
        conn.close()
        return JenisModel.row_to_entity(row) if row else None

    @staticmethod
    def insert(nama: str) -> int:
        conn = get_connection()
        cur = conn.execute("INSERT INTO jenis (nama) VALUES (?)", (nama,))
        conn.commit()
        last_id = cur.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def update(id_: int, nama: str) -> bool:
        conn = get_connection()
        cur = conn.execute("UPDATE jenis SET nama = ? WHERE id = ?", (nama, id_))
        conn.commit()
        affected = cur.rowcount
        conn.close()
        return affected > 0

    @staticmethod
    def delete(id_: int) -> bool:
        conn = get_connection()
        cur = conn.execute("DELETE FROM jenis WHERE id = ?", (id_,))
        conn.commit()
        affected = cur.rowcount
        conn.close()
        return affected > 0
