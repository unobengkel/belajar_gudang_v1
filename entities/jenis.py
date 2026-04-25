"""entities/jenis.py — Entity Jenis"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Jenis:
    id: Optional[int]
    nama: str
