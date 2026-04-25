"""repositories/merek_repository.py"""
from models.merek_model import MerekModel
from entities.merek import Merek
from typing import List, Optional


class MerekRepository:
    def get_all(self) -> List[Merek]:
        return MerekModel.find_all()

    def get_by_id(self, id_: int) -> Optional[Merek]:
        return MerekModel.find_by_id(id_)

    def create(self, nama: str) -> int:
        return MerekModel.insert(nama)

    def update(self, id_: int, nama: str) -> bool:
        return MerekModel.update(id_, nama)

    def delete(self, id_: int) -> bool:
        return MerekModel.delete(id_)
