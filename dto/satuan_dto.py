"""dto/satuan_dto.py — Data Transfer Objects untuk Satuan"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class SatuanCreateDTO:
    nama: str

    @staticmethod
    def from_form(data: dict) -> "SatuanCreateDTO":
        nama = data.get("nama", "").strip()
        if not nama:
            raise ValueError("Nama satuan tidak boleh kosong.")
        return SatuanCreateDTO(nama=nama)


@dataclass
class SatuanUpdateDTO:
    id: int
    nama: str

    @staticmethod
    def from_form(data: dict) -> "SatuanUpdateDTO":
        try:
            id_ = int(data.get("id", 0))
        except (ValueError, TypeError):
            raise ValueError("ID tidak valid.")
        nama = data.get("nama", "").strip()
        if not nama:
            raise ValueError("Nama satuan tidak boleh kosong.")
        return SatuanUpdateDTO(id=id_, nama=nama)


@dataclass
class SatuanResponseDTO:
    id: int
    nama: str
