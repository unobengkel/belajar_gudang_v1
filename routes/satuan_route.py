"""routes/satuan_route.py — HTTP handler Satuan"""
from routes.base_route import render_template, parse_form_data, send_html, redirect
from services.satuan_service import SatuanService
from dto.satuan_dto import SatuanCreateDTO, SatuanUpdateDTO


_service = SatuanService()


def handle_get(handler):
    items = _service.get_all()
    html = render_template("satuan/index.html", items=items, error=None, success=None)
    send_html(handler, html)


def handle_post(handler, action: str):
    data = parse_form_data(handler)
    try:
        if action == "add":
            dto = SatuanCreateDTO.from_form(data)
            _service.create(dto)
        elif action == "edit":
            dto = SatuanUpdateDTO.from_form(data)
            _service.update(dto)
        elif action == "delete":
            id_ = int(data.get("id", 0))
            _service.delete(id_)
    except Exception as e:
        items = _service.get_all()
        html = render_template("satuan/index.html", items=items, error=str(e), success=None)
        send_html(handler, html)
        return
    redirect(handler, "/satuan")
