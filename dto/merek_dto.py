"""dto/merek_dto.py — Data Transfer Objects untuk Merek"""
from dataclasses import dataclass


@dataclass
class MerekCreateDTO:
    nama: str

    @staticmethod
    def from_form(data: dict) -> "MerekCreateDTO":
        nama = data.get("nama", "").strip()
        if not nama:
            raise ValueError("Nama merek tidak boleh kosong.")
        return MerekCreateDTO(nama=nama)


@dataclass
class MerekUpdateDTO:
    id: int
    nama: str

    @staticmethod
    def from_form(data: dict) -> "MerekUpdateDTO":
        try:
            id_ = int(data.get("id", 0))
        except (ValueError, TypeError):
            raise ValueError("ID tidak valid.")
        nama = data.get("nama", "").strip()
        if not nama:
            raise ValueError("Nama merek tidak boleh kosong.")
        return MerekUpdateDTO(id=id_, nama=nama)


@dataclass
class MerekResponseDTO:
    id: int
    nama: str
