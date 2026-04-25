"""entities/merek.py — Entity Merek"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Merek:
    id: Optional[int]
    nama: str
