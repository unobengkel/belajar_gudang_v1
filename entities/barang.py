"""entities/barang.py — Entity Barang"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Barang:
    id: Optional[int]
    nama: str
    idjenis: Optional[int]
    idsatuan: Optional[int]
    idmerek: Optional[int]
    # Read-only display fields (joined from relation)
    nama_jenis: Optional[str] = None
    nama_satuan: Optional[str] = None
    nama_merek: Optional[str] = None
