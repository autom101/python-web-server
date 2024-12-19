import BaseHTTPServer

class HTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  # Handle GET requests
  def do_GET(self):
    self.send_response(200)