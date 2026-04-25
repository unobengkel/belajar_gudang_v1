"""repositories/satuan_repository.py"""
from models.satuan_model import SatuanModel
from entities.satuan import Satuan
from typing import List, Optional


class SatuanRepository:
    def get_all(self) -> List[Satuan]:
        return SatuanModel.find_all()

    def get_by_id(self, id_: int) -> Optional[Satuan]:
        return SatuanModel.find_by_id(id_)

    def create(self, nama: str) -> int:
        return SatuanModel.insert(nama)

    def update(self, id_: int, nama: str) -> bool:
        return SatuanModel.update(id_, nama)

    def delete(self, id_: int) -> bool:
        return SatuanModel.delete(id_)
