"""repositories/barang_repository.py"""
from models.barang_model import BarangModel
from entities.barang import Barang
from typing import List, Optional


class BarangRepository:
    def get_all(self) -> List[Barang]:
        return BarangModel.find_all()

    def get_by_id(self, id_: int) -> Optional[Barang]:
        return BarangModel.find_by_id(id_)

    def create(self, nama: str, idjenis, idsatuan, idmerek) -> int:
        return BarangModel.insert(nama, idjenis, idsatuan, idmerek)

    def update(self, id_: int, nama: str, idjenis, idsatuan, idmerek) -> bool:
        return BarangModel.update(id_, nama, idjenis, idsatuan, idmerek)

    def delete(self, id_: int) -> bool:
        return BarangModel.delete(id_)
