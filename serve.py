#!/usr/bin/env python3
"""Dev server: rebuilds on file change, serves build/ on http://localhost:8000."""

import http.server
import socketserver
import threading
import time
import traceback
from pathlib import Path

from nescribe import build, BUILD_DIR

WATCH_DIRS = [Path("content"), Path("site"), Path("images")]
PORT = 8080


def snapshot() -> dict:
    return {
        p: p.stat().st_mtime
        for d in WATCH_DIRS if d.exists()
        for p in d.rglob("*") if p.is_file()
    }


def watch():
    last = snapshot()
    while True:
        time.sleep(0.5)
        current = snapshot()
        if current != last:
            last = current
            try:
                build()
            except Exception:
                traceback.print_exc()


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BUILD_DIR), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    build()
    threading.Thread(target=watch, daemon=True).start()
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving http://localhost:{PORT}  (watching {', '.join(str(d) for d in WATCH_DIRS)})")
        httpd.serve_forever()
