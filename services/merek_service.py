"""services/merek_service.py — Business logic Merek"""
from repositories.merek_repository import MerekRepository
from dto.merek_dto import MerekCreateDTO, MerekUpdateDTO, MerekResponseDTO
from typing import List, Optional


class MerekService:
    def __init__(self):
        self.repo = MerekRepository()

    def get_all(self) -> List[MerekResponseDTO]:
        items = self.repo.get_all()
        return [MerekResponseDTO(id=i.id, nama=i.nama) for i in items]

    def get_by_id(self, id_: int) -> Optional[MerekResponseDTO]:
        item = self.repo.get_by_id(id_)
        return MerekResponseDTO(id=item.id, nama=item.nama) if item else None

    def create(self, dto: MerekCreateDTO) -> int:
        return self.repo.create(dto.nama)

    def update(self, dto: MerekUpdateDTO) -> bool:
        return self.repo.update(dto.id, dto.nama)

    def delete(self, id_: int) -> bool:
        return self.repo.delete(id_)
