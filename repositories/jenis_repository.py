"""repositories/jenis_repository.py"""
from models.jenis_model import JenisModel
from entities.jenis import Jenis
from typing import List, Optional


class JenisRepository:
    def get_all(self) -> List[Jenis]:
        return JenisModel.find_all()

    def get_by_id(self, id_: int) -> Optional[Jenis]:
        return JenisModel.find_by_id(id_)

    def create(self, nama: str) -> int:
        return JenisModel.insert(nama)

    def update(self, id_: int, nama: str) -> bool:
        return JenisModel.update(id_, nama)

    def delete(self, id_: int) -> bool:
        return JenisModel.delete(id_)
