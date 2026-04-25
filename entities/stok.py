"""entities/stok.py — Entity Stok"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Stok:
    id: Optional[int]
    idbarang: int
    jumlah: float
    datetime: str
    # Read-only display fields (joined from relation)
    nama_barang: Optional[str] = None
    nama_satuan: Optional[str] = None
