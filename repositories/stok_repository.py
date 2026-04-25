"""repositories/stok_repository.py"""
from models.stok_model import StokModel
from entities.stok import Stok
from typing import List, Optional


class StokRepository:
    def get_all(self) -> List[Stok]:
        return StokModel.find_all()

    def get_by_id(self, id_: int) -> Optional[Stok]:
        return StokModel.find_by_id(id_)

    def create(self, idbarang: int, jumlah: float, datetime_: str) -> int:
        return StokModel.insert(idbarang, jumlah, datetime_)

    def update(self, id_: int, idbarang: int, jumlah: float, datetime_: str) -> bool:
        return StokModel.update(id_, idbarang, jumlah, datetime_)

    def delete(self, id_: int) -> bool:
        return StokModel.delete(id_)

    def summary_per_barang(self) -> List[dict]:
        return StokModel.summary_per_barang()
