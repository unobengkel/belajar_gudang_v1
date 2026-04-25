"""routes/stok_route.py — HTTP handler Stok"""
from routes.base_route import render_template, parse_form_data, send_html, redirect
from services.stok_service import StokService
from services.barang_service import BarangService
from dto.stok_dto import StokCreateDTO, StokUpdateDTO


_service = StokService()
_barang_svc = BarangService()


def handle_get(handler):
    items = _service.get_all()
    barang_list = _barang_svc.get_all()
    summary = _service.summary_per_barang()
    html = render_template(
        "stok/index.html",
        items=items,
        barang_list=barang_list,
        summary=summary,
        error=None,
    )
    send_html(handler, html)


def handle_post(handler, action: str):
    data = parse_form_data(handler)
    try:
        if action == "add":
            dto = StokCreateDTO.from_form(data)
            _service.create(dto)
        elif action == "edit":
            dto = StokUpdateDTO.from_form(data)
            _service.update(dto)
        elif action == "delete":
            id_ = int(data.get("id", 0))
            _service.delete(id_)
    except Exception as e:
        items = _service.get_all()
        barang_list = _barang_svc.get_all()
        summary = _service.summary_per_barang()
        html = render_template(
            "stok/index.html",
            items=items,
            barang_list=barang_list,
            summary=summary,
            error=str(e),
        )
        send_html(handler, html)
        return
    redirect(handler, "/stok")
