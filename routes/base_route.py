"""
routes/base_route.py
Base class dan utilitas untuk semua route handler.
"""
import json
import urllib.parse
from http.server import BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader
import os

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")

_jinja_env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=True,
)


def render_template(template_path: str, **context) -> str:
    """Render template Jinja2 dan kembalikan string HTML."""
    tmpl = _jinja_env.get_template(template_path)
    return tmpl.render(**context)


def parse_form_data(handler: BaseHTTPRequestHandler) -> dict:
    """Membaca body POST dan mengembalikan dict."""
    length = int(handler.headers.get("Content-Length", 0))
    body = handler.rfile.read(length).decode("utf-8")
    return dict(urllib.parse.parse_qsl(body))


def send_html(handler: BaseHTTPRequestHandler, html: str, status: int = 200) -> None:
    handler.send_response(status)
    handler.send_header("Content-Type", "text/html; charset=utf-8")
    handler.end_headers()
    handler.wfile.write(html.encode("utf-8"))


def redirect(handler: BaseHTTPRequestHandler, location: str) -> None:
    handler.send_response(302)
    handler.send_header("Location", location)
    handler.end_headers()
