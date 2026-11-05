import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"Hola desde SO2 - pod: {socket.gethostname()}\n".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)

HTTPServer(("0.0.0.0", 8080), H).serve_forever()
