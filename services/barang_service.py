"""services/barang_service.py — Business logic Barang"""
from repositories.barang_repository import BarangRepository
from dto.barang_dto import BarangCreateDTO, BarangUpdateDTO, BarangResponseDTO
from typing import List, Optional


class BarangService:
    def __init__(self):
        self.repo = BarangRepository()

    def get_all(self) -> List[BarangResponseDTO]:
        items = self.repo.get_all()
        return [
            BarangResponseDTO(
                id=i.id, nama=i.nama,
                idjenis=i.idjenis, idsatuan=i.idsatuan, idmerek=i.idmerek,
                nama_jenis=i.nama_jenis, nama_satuan=i.nama_satuan, nama_merek=i.nama_merek,
            )
            for i in items
        ]

    def get_by_id(self, id_: int) -> Optional[BarangResponseDTO]:
        i = self.repo.get_by_id(id_)
        if not i:
            return None
        return BarangResponseDTO(
            id=i.id, nama=i.nama,
            idjenis=i.idjenis, idsatuan=i.idsatuan, idmerek=i.idmerek,
            nama_jenis=i.nama_jenis, nama_satuan=i.nama_satuan, nama_merek=i.nama_merek,
        )

    def create(self, dto: BarangCreateDTO) -> int:
        return self.repo.create(dto.nama, dto.idjenis, dto.idsatuan, dto.idmerek)

    def update(self, dto: BarangUpdateDTO) -> bool:
        return self.repo.update(dto.id, dto.nama, dto.idjenis, dto.idsatuan, dto.idmerek)

    def delete(self, id_: int) -> bool:
        return self.repo.delete(id_)
