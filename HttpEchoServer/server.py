from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _get_payload(self):
        payload_size = int(self.headers['Content-Length'])
        return self.rfile.read(payload_size).decode()

    def do_GET(self):
        payload = self._get_payload()
        self._set_headers()
        self.wfile.write("GET request for {} with payload: {}".format(self.path, payload).encode('utf-8'))

    def do_POST(self):
        payload = self._get_payload()
        self._set_headers()
        self.wfile.write("POST request for {} with payload: {}".format(self.path, payload).encode('utf-8'))

    def do_PUT(self):
        payload = self._get_payload()
        self._set_headers()
        self.wfile.write("PUT request for {} with payload: {}".format(self.path, payload).encode('utf-8'))

    def do_DELETE(self):
        payload = self._get_payload()
        self._set_headers()
        self.wfile.write("DELETE request for {} with payload: {}".format(self.path, payload).encode('utf-8'))


if __name__ == "__main__":
    server = HTTPServer(('', 80), HTTPRequestHandler)
    print('HttpEchoServer started')
    server.serve_forever()
