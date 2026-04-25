"""
main.py
Entry point server HTTP untuk Gudang V1.
Menangani routing, menghubungkan semua layer.
"""
import sys
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

# Pastikan root project ada di sys.path
sys.path.insert(0, os.path.dirname(__file__))

from database import init_db
from routes.base_route import render_template, send_html, redirect
from routes import jenis_route, satuan_route, merek_route, barang_route, stok_route
from services.jenis_service import JenisService
from services.satuan_service import SatuanService
from services.merek_service import MerekService
from services.barang_service import BarangService
from services.stok_service import StokService

HOST = "localhost"
PORT = 8080


class GudangHandler(BaseHTTPRequestHandler):
    """Main HTTP handler — routing semua request GET dan POST."""

    # ------------------------------------------------------------------ #
    #  GET Handler
    # ------------------------------------------------------------------ #
    def do_GET(self):
        path = urlparse(self.path).path.rstrip("/") or "/"

        if path == "/":
            self._handle_dashboard()
        elif path == "/jenis":
            jenis_route.handle_get(self)
        elif path == "/satuan":
            satuan_route.handle_get(self)
        elif path == "/merek":
            merek_route.handle_get(self)
        elif path == "/barang":
            barang_route.handle_get(self)
        elif path == "/stok":
            stok_route.handle_get(self)
        else:
            self._send_404()

    # ------------------------------------------------------------------ #
    #  POST Handler
    # ------------------------------------------------------------------ #
    def do_POST(self):
        path = urlparse(self.path).path

        routes_map = {
            "/jenis/add":    ("jenis",   "add"),
            "/jenis/edit":   ("jenis",   "edit"),
            "/jenis/delete": ("jenis",   "delete"),
            "/satuan/add":   ("satuan",  "add"),
            "/satuan/edit":  ("satuan",  "edit"),
            "/satuan/delete":("satuan",  "delete"),
            "/merek/add":    ("merek",   "add"),
            "/merek/edit":   ("merek",   "edit"),
            "/merek/delete": ("merek",   "delete"),
            "/barang/add":   ("barang",  "add"),
            "/barang/edit":  ("barang",  "edit"),
            "/barang/delete":("barang",  "delete"),
            "/stok/add":     ("stok",    "add"),
            "/stok/edit":    ("stok",    "edit"),
            "/stok/delete":  ("stok",    "delete"),
        }

        if path not in routes_map:
            self._send_404()
            return

        entity, action = routes_map[path]
        handler_map = {
            "jenis":  jenis_route.handle_post,
            "satuan": satuan_route.handle_post,
            "merek":  merek_route.handle_post,
            "barang": barang_route.handle_post,
            "stok":   stok_route.handle_post,
        }
        handler_map[entity](self, action)

    # ------------------------------------------------------------------ #
    #  Dashboard
    # ------------------------------------------------------------------ #
    def _handle_dashboard(self):
        jenis_svc  = JenisService()
        satuan_svc = SatuanService()
        merek_svc  = MerekService()
        barang_svc = BarangService()
        stok_svc   = StokService()

        icon_jenis = '<svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A2 2 0 013 12V7a2 2 0 012-2z"/></svg>'
        icon_satuan = '<svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>'
        icon_merek = '<svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>'
        icon_barang = '<svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0H4m8-7v7"/></svg>'

        stats = [
            {"label": "Jenis Barang", "count": len(jenis_svc.get_all()),  "url": "/jenis",  "color": "bg-violet-500", "icon": icon_jenis},
            {"label": "Satuan",       "count": len(satuan_svc.get_all()), "url": "/satuan", "color": "bg-sky-500",    "icon": icon_satuan},
            {"label": "Merek",        "count": len(merek_svc.get_all()),  "url": "/merek",  "color": "bg-amber-500",  "icon": icon_merek},
            {"label": "Total Barang", "count": len(barang_svc.get_all()), "url": "/barang", "color": "bg-brand-500",  "icon": icon_barang},
        ]

        summary = stok_svc.summary_per_barang()
        html = render_template("index.html", stats=stats, summary=summary, active_page="dashboard")
        send_html(self, html)

    # ------------------------------------------------------------------ #
    #  Utilities
    # ------------------------------------------------------------------ #
    def _send_404(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"<h1>404 - Halaman tidak ditemukan</h1>")

    def log_message(self, fmt, *args):
        """Override agar log lebih bersih."""
        print(f"  [{self.address_string()}] {fmt % args}")


# ------------------------------------------------------------------ #
#  Entry Point
# ------------------------------------------------------------------ #
if __name__ == "__main__":
    init_db()
    server = HTTPServer((HOST, PORT), GudangHandler)
    print(f"\n{'='*50}")
    print(f"  [SERVER] Gudang V1")
    print(f"  [URL]    http://{HOST}:{PORT}")
    print(f"{'='*50}")
    print("  Tekan Ctrl+C untuk menghentikan server.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server dihentikan.")
        server.server_close()
