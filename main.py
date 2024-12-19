from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPRequestHandler(BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        self.send_response(200)


if __name__ == '__main__':
    serverAddress = ('', 3000)
    server = HTTPServer(serverAddress, HTTPRequestHandler)
    server.serve_forever()
