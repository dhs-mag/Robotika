from http.server import SimpleHTTPRequestHandler
import socketserver
import re
import json


class CustomHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        if None != re.search('/api/sonar', self.path):

            if None != self.server.sonar:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                json_response = {
                    'status': 'ok',
                    'sonar': {
                        'distance': self.server.sonar.get_distance(),
                        'segments': self.server.sonar.get_segments(),
                        'viewAngle': self.server.sonar.get_view_angle()
                    }
                }
                self.wfile.write(json.dumps(json_response).encode())
            else:
                self.send_response(500)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write("Sonar is not loaded".encode())

        else:
            SimpleHTTPRequestHandler.do_GET(self)


class CustomTCPServer(socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass, sonar):
        super().__init__(server_address, RequestHandlerClass)
        self.sonar = sonar


class Server:
# TODO implement here sonar webserver preview
    def __init__(self, port):
        self.sonar = None
        self.port = port
        self.handler = None

    def run(self):
        if None == self.sonar:
            print("Please set sonar first")
        else:
            with CustomTCPServer(("", self.port), CustomHandler, self.sonar) as httpd:
                print("serving at port", self.port)
                httpd.serve_forever()

    def set_sonar(self, sonar):
        self.sonar = sonar

