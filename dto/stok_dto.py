"""dto/stok_dto.py — Data Transfer Objects untuk Stok"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class StokCreateDTO:
    idbarang: int
    jumlah: float
    datetime: str

    @staticmethod
    def from_form(data: dict) -> "StokCreateDTO":
        try:
            idbarang = int(data.get("idbarang", 0))
            if idbarang <= 0:
                raise ValueError()
        except (ValueError, TypeError):
            raise ValueError("Barang harus dipilih.")

        try:
            jumlah = float(data.get("jumlah", 0))
        except (ValueError, TypeError):
            raise ValueError("Jumlah tidak valid.")

        dt = data.get("datetime", "").strip()
        if not dt:
            raise ValueError("Datetime tidak boleh kosong.")

        return StokCreateDTO(idbarang=idbarang, jumlah=jumlah, datetime=dt)


@dataclass
class StokUpdateDTO:
    id: int
    idbarang: int
    jumlah: float
    datetime: str

    @staticmethod
    def from_form(data: dict) -> "StokUpdateDTO":
        try:
            id_ = int(data.get("id", 0))
        except (ValueError, TypeError):
            raise ValueError("ID tidak valid.")

        try:
            idbarang = int(data.get("idbarang", 0))
            if idbarang <= 0:
                raise ValueError()
        except (ValueError, TypeError):
            raise ValueError("Barang harus dipilih.")

        try:
            jumlah = float(data.get("jumlah", 0))
        except (ValueError, TypeError):
            raise ValueError("Jumlah tidak valid.")

        dt = data.get("datetime", "").strip()
        if not dt:
            raise ValueError("Datetime tidak boleh kosong.")

        return StokUpdateDTO(id=id_, idbarang=idbarang, jumlah=jumlah, datetime=dt)


@dataclass
class StokResponseDTO:
    id: int
    idbarang: int
    jumlah: float
    datetime: str
    nama_barang: Optional[str]
    nama_satuan: Optional[str]
