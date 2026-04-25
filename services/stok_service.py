"""services/stok_service.py — Business logic Stok"""
from repositories.stok_repository import StokRepository
from dto.stok_dto import StokCreateDTO, StokUpdateDTO, StokResponseDTO
from typing import List, Optional


class StokService:
    def __init__(self):
        self.repo = StokRepository()

    def get_all(self) -> List[StokResponseDTO]:
        items = self.repo.get_all()
        return [
            StokResponseDTO(
                id=i.id, idbarang=i.idbarang, jumlah=i.jumlah, datetime=i.datetime,
                nama_barang=i.nama_barang, nama_satuan=i.nama_satuan,
            )
            for i in items
        ]

    def get_by_id(self, id_: int) -> Optional[StokResponseDTO]:
        i = self.repo.get_by_id(id_)
        if not i:
            return None
        return StokResponseDTO(
            id=i.id, idbarang=i.idbarang, jumlah=i.jumlah, datetime=i.datetime,
            nama_barang=i.nama_barang, nama_satuan=i.nama_satuan,
        )

    def create(self, dto: StokCreateDTO) -> int:
        return self.repo.create(dto.idbarang, dto.jumlah, dto.datetime)

    def update(self, dto: StokUpdateDTO) -> bool:
        return self.repo.update(dto.id, dto.idbarang, dto.jumlah, dto.datetime)

    def delete(self, id_: int) -> bool:
        return self.repo.delete(id_)

    def summary_per_barang(self) -> List[dict]:
        return self.repo.summary_per_barang()
