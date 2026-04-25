"""entities/satuan.py — Entity Satuan"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Satuan:
    id: Optional[int]
    nama: str
