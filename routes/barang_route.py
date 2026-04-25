"""routes/barang_route.py — HTTP handler Barang"""
from routes.base_route import render_template, parse_form_data, send_html, redirect
from services.barang_service import BarangService
from services.jenis_service import JenisService
from services.satuan_service import SatuanService
from services.merek_service import MerekService
from dto.barang_dto import BarangCreateDTO, BarangUpdateDTO


_service = BarangService()
_jenis_svc = JenisService()
_satuan_svc = SatuanService()
_merek_svc = MerekService()


def _get_dropdowns():
    return {
        "jenis_list": _jenis_svc.get_all(),
        "satuan_list": _satuan_svc.get_all(),
        "merek_list": _merek_svc.get_all(),
    }


def handle_get(handler):
    items = _service.get_all()
    html = render_template("barang/index.html", items=items, error=None, **_get_dropdowns())
    send_html(handler, html)


def handle_post(handler, action: str):
    data = parse_form_data(handler)
    try:
        if action == "add":
            dto = BarangCreateDTO.from_form(data)
            _service.create(dto)
        elif action == "edit":
            dto = BarangUpdateDTO.from_form(data)
            _service.update(dto)
        elif action == "delete":
            id_ = int(data.get("id", 0))
            _service.delete(id_)
    except Exception as e:
        items = _service.get_all()
        html = render_template("barang/index.html", items=items, error=str(e), **_get_dropdowns())
        send_html(handler, html)
        return
    redirect(handler, "/barang")
