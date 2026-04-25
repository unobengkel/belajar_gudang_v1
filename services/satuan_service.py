"""services/satuan_service.py — Business logic Satuan"""
from repositories.satuan_repository import SatuanRepository
from dto.satuan_dto import SatuanCreateDTO, SatuanUpdateDTO, SatuanResponseDTO
from entities.satuan import Satuan
from typing import List, Optional


class SatuanService:
    def __init__(self):
        self.repo = SatuanRepository()

    def get_all(self) -> List[SatuanResponseDTO]:
        items = self.repo.get_all()
        return [SatuanResponseDTO(id=i.id, nama=i.nama) for i in items]

    def get_by_id(self, id_: int) -> Optional[SatuanResponseDTO]:
        item = self.repo.get_by_id(id_)
        return SatuanResponseDTO(id=item.id, nama=item.nama) if item else None

    def create(self, dto: SatuanCreateDTO) -> int:
        return self.repo.create(dto.nama)

    def update(self, dto: SatuanUpdateDTO) -> bool:
        return self.repo.update(dto.id, dto.nama)

    def delete(self, id_: int) -> bool:
        return self.repo.delete(id_)
