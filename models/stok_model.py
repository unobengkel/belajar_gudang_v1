"""models/stok_model.py — SQL model mapping untuk Stok"""
from database import get_connection
from entities.stok import Stok
from typing import List, Optional


_JOIN_SQL = """
    SELECT sk.id, sk.idbarang, sk.jumlah, sk.datetime,
           b.nama  AS nama_barang,
           s.nama  AS nama_satuan
    FROM stok sk
    JOIN barang  b ON b.id  = sk.idbarang
    LEFT JOIN satuan  s ON s.id  = b.idsatuan
"""


class StokModel:
    @staticmethod
    def row_to_entity(row) -> Stok:
        return Stok(
            id=row["id"],
            idbarang=row["idbarang"],
            jumlah=row["jumlah"],
            datetime=row["datetime"],
            nama_barang=row["nama_barang"],
            nama_satuan=row["nama_satuan"],
        )

    @staticmethod
    def find_all() -> List[Stok]:
        conn = get_connection()
        rows = conn.execute(_JOIN_SQL + " ORDER BY sk.datetime DESC").fetchall()
        conn.close()
        return [StokModel.row_to_entity(r) for r in rows]

    @staticmethod
    def find_by_id(id_: int) -> Optional[Stok]:
        conn = get_connection()
        row = conn.execute(_JOIN_SQL + " WHERE sk.id = ?", (id_,)).fetchone()
        conn.close()
        return StokModel.row_to_entity(row) if row else None

    @staticmethod
    def insert(idbarang: int, jumlah: float, datetime_: str) -> int:
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO stok (idbarang, jumlah, datetime) VALUES (?,?,?)",
            (idbarang, jumlah, datetime_),
        )
        conn.commit()
        last_id = cur.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def update(id_: int, idbarang: int, jumlah: float, datetime_: str) -> bool:
        conn = get_connection()
        cur = conn.execute(
            "UPDATE stok SET idbarang=?, jumlah=?, datetime=? WHERE id=?",
            (idbarang, jumlah, datetime_, id_),
        )
        conn.commit()
        affected = cur.rowcount
        conn.close()
        return affected > 0

    @staticmethod
    def delete(id_: int) -> bool:
        conn = get_connection()
        cur = conn.execute("DELETE FROM stok WHERE id = ?", (id_,))
        conn.commit()
        affected = cur.rowcount
        conn.close()
        return affected > 0

    @staticmethod
    def summary_per_barang() -> List[dict]:
        """Ringkasan total stok per barang."""
        conn = get_connection()
        rows = conn.execute("""
            SELECT b.id, b.nama AS nama_barang,
                   s.nama AS nama_satuan,
                   COALESCE(SUM(sk.jumlah), 0) AS total_stok
            FROM barang b
            LEFT JOIN satuan s ON s.id = b.idsatuan
            LEFT JOIN stok sk ON sk.idbarang = b.id
            GROUP BY b.id
            ORDER BY b.nama
        """).fetchall()
        conn.close()
        return [dict(r) for r in rows]
