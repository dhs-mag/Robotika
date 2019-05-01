#!usr/bin/env python3
import json
import os
import re
import socketserver
import threading
from http.server import SimpleHTTPRequestHandler


class CustomHandler(SimpleHTTPRequestHandler):

    def log_message(self, format, *args):
        return

    def do_GET(self):
        if None != re.search('/api/move', self.path):

            if None != self.server.driving:
                if None != re.search('/forward', self.path):
                    self.server.driving.forward()
                elif None != re.search('/left', self.path):
                    self.server.driving.left()
                elif None != re.search('/back', self.path):
                    self.server.driving.back()
                elif None != re.search('/right', self.path):
                    self.server.driving.right()
                elif None != re.search('/stop', self.path):
                    self.server.driving.stop()

                self.send_response(200)
                json_response = {
                    'status': 'ok'
                }
            else:
                self.send_response(500)
                json_response = {
                    'status': 'failed',
                    'message': 'Driving is not loaded'
                }

            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Headers', '*')
            self.send_header('Access-Control-Allow-Methods', '*')
            self.end_headers()
            self.wfile.write(json.dumps(json_response).encode())

        elif None != re.search('/api/auto', self.path):
            if None != self.server.navigator:
                if None != re.search('/start', self.path):
                    self.server.navigator.start_nav()
                elif None != re.search('/stop', self.path):
                    self.server.navigator.stop_nav()

                self.send_response(200)
                json_response = {
                    'status': 'ok'
                }
            else:
                self.send_response(500)
                json_response = {
                    'status': 'failed',
                    'message': 'Navigator is not loaded'
                }

            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Headers', '*')
            self.send_header('Access-Control-Allow-Methods', '*')
            self.end_headers()
            self.wfile.write(json.dumps(json_response).encode())

        elif None != re.search('/api/sonar', self.path):

            if None != self.server.sonar:
                self.send_response(200)
                json_response = {
                    'status': 'ok',
                    'sonar': {
                        'distance': self.server.sonar.get_distance(),
                        'segments': self.server.sonar.get_segments(),
                        'viewAngle': self.server.sonar.get_view_angle()
                    }
                }
            else:
                self.send_response(500)
                json_response = {
                    'status': 'failed',
                    'message': 'Sonar is not loaded'
                }

            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Headers', '*')
            self.send_header('Access-Control-Allow-Methods', '*')
            self.end_headers()
            self.wfile.write(json.dumps(json_response).encode())

        else:
            SimpleHTTPRequestHandler.do_GET(self)


class CustomTCPServer(socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass, sonar, driving, navigator):
        super().__init__(server_address, RequestHandlerClass)
        self.sonar = sonar
        self.driving = driving
        self.navigator = navigator


class Server:

    def __init__(self, port):
        self.sonar = None
        self.driving = None
        self.navigator = None
        self.port = port
        self.handler = None
        # self.httpd = None

    def run(self):
        web_dir = os.path.join(os.path.dirname(__file__), '../dev/fe/dist')
        os.chdir(web_dir)
        if None == self.sonar:
            print("Please set sonar first")
        else:
            httpd = None
            try:
                httpd = CustomTCPServer(("", self.port), CustomHandler, self.sonar, self.driving, self.navigator)
                print("serving at port", self.port)
                httpd.serve_forever()
            except Exception:
                if httpd is not None:
                    print('server shutdown')
                    threading.Thread(target=httpd.shutdown, daemon=True).start()
                # httpd.shutdown()
                # httpd = CustomTCPServer(("", self.port), CustomHandler, self.sonar, self.driving)

    def set_sonar(self, sonar):
        self.sonar = sonar

    def set_driving(self, driving):
        self.driving = driving

    def set_navigator(self, navigator):
        self.navigator = navigator
