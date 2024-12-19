from http.server import BaseHTTPRequestHandler


class HTTPRequestHandler(BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        self.send_response(200)
