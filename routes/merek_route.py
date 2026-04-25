"""routes/merek_route.py — HTTP handler Merek"""
from routes.base_route import render_template, parse_form_data, send_html, redirect
from services.merek_service import MerekService
from dto.merek_dto import MerekCreateDTO, MerekUpdateDTO


_service = MerekService()


def handle_get(handler):
    items = _service.get_all()
    html = render_template("merek/index.html", items=items, error=None, success=None)
    send_html(handler, html)


def handle_post(handler, action: str):
    data = parse_form_data(handler)
    try:
        if action == "add":
            dto = MerekCreateDTO.from_form(data)
            _service.create(dto)
        elif action == "edit":
            dto = MerekUpdateDTO.from_form(data)
            _service.update(dto)
        elif action == "delete":
            id_ = int(data.get("id", 0))
            _service.delete(id_)
    except Exception as e:
        items = _service.get_all()
        html = render_template("merek/index.html", items=items, error=str(e), success=None)
        send_html(handler, html)
        return
    redirect(handler, "/merek")
