"""services/jenis_service.py — Business logic Jenis"""
from repositories.jenis_repository import JenisRepository
from dto.jenis_dto import JenisCreateDTO, JenisUpdateDTO, JenisResponseDTO
from typing import List, Optional


class JenisService:
    def __init__(self):
        self.repo = JenisRepository()

    def get_all(self) -> List[JenisResponseDTO]:
        items = self.repo.get_all()
        return [JenisResponseDTO(id=i.id, nama=i.nama) for i in items]

    def get_by_id(self, id_: int) -> Optional[JenisResponseDTO]:
        item = self.repo.get_by_id(id_)
        return JenisResponseDTO(id=item.id, nama=item.nama) if item else None

    def create(self, dto: JenisCreateDTO) -> int:
        return self.repo.create(dto.nama)

    def update(self, dto: JenisUpdateDTO) -> bool:
        return self.repo.update(dto.id, dto.nama)

    def delete(self, id_: int) -> bool:
        return self.repo.delete(id_)
