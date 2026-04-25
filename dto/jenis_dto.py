"""dto/jenis_dto.py — Data Transfer Objects untuk Jenis"""
from dataclasses import dataclass


@dataclass
class JenisCreateDTO:
    nama: str

    @staticmethod
    def from_form(data: dict) -> "JenisCreateDTO":
        nama = data.get("nama", "").strip()
        if not nama:
            raise ValueError("Nama jenis tidak boleh kosong.")
        return JenisCreateDTO(nama=nama)


@dataclass
class JenisUpdateDTO:
    id: int
    nama: str

    @staticmethod
    def from_form(data: dict) -> "JenisUpdateDTO":
        try:
            id_ = int(data.get("id", 0))
        except (ValueError, TypeError):
            raise ValueError("ID tidak valid.")
        nama = data.get("nama", "").strip()
        if not nama:
            raise ValueError("Nama jenis tidak boleh kosong.")
        return JenisUpdateDTO(id=id_, nama=nama)


@dataclass
class JenisResponseDTO:
    id: int
    nama: str
