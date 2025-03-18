from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 3000

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.end_headers()
            print(self.headers)

with HTTPServer(('', PORT), RequestHandler) as httpd:
    httpd.serve_forever()