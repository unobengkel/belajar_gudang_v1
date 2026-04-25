"""dto/barang_dto.py — Data Transfer Objects untuk Barang"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class BarangCreateDTO:
    nama: str
    idjenis: Optional[int]
    idsatuan: Optional[int]
    idmerek: Optional[int]

    @staticmethod
    def from_form(data: dict) -> "BarangCreateDTO":
        nama = data.get("nama", "").strip()
        if not nama:
            raise ValueError("Nama barang tidak boleh kosong.")

        def to_int_or_none(val):
            try:
                v = int(val)
                return v if v > 0 else None
            except (ValueError, TypeError):
                return None

        return BarangCreateDTO(
            nama=nama,
            idjenis=to_int_or_none(data.get("idjenis")),
            idsatuan=to_int_or_none(data.get("idsatuan")),
            idmerek=to_int_or_none(data.get("idmerek")),
        )


@dataclass
class BarangUpdateDTO:
    id: int
    nama: str
    idjenis: Optional[int]
    idsatuan: Optional[int]
    idmerek: Optional[int]

    @staticmethod
    def from_form(data: dict) -> "BarangUpdateDTO":
        try:
            id_ = int(data.get("id", 0))
        except (ValueError, TypeError):
            raise ValueError("ID tidak valid.")

        nama = data.get("nama", "").strip()
        if not nama:
            raise ValueError("Nama barang tidak boleh kosong.")

        def to_int_or_none(val):
            try:
                v = int(val)
                return v if v > 0 else None
            except (ValueError, TypeError):
                return None

        return BarangUpdateDTO(
            id=id_,
            nama=nama,
            idjenis=to_int_or_none(data.get("idjenis")),
            idsatuan=to_int_or_none(data.get("idsatuan")),
            idmerek=to_int_or_none(data.get("idmerek")),
        )


@dataclass
class BarangResponseDTO:
    id: int
    nama: str
    idjenis: Optional[int]
    idsatuan: Optional[int]
    idmerek: Optional[int]
    nama_jenis: Optional[str]
    nama_satuan: Optional[str]
    nama_merek: Optional[str]
