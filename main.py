import json
from http.server import BaseHTTPRequestHandler, HTTPServer

planets = [
    {
        "name": "Земля",
        "type": "Каменистая планета",
        "distance": "149,6 млн км"
    },
    {
        "name": "Марс",
        "type": "Каменистая планета",
        "distance": "227,9 млн км"
    },
    {
        "name": "Юпитер",
        "type": "Газовый гигант",
        "distance": "778,5 млн км"
    }
]


class PlanetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/planets':
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()

            json_data = json.dumps(planets, ensure_ascii=False)
            self.wfile.write(json_data.encode('utf-8'))
        else:
            self.send_error(404, "Not Found")


def run():
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, PlanetHandler)
    print("Сервер запущен. Проверьте http://127.0.0.1:8000/planets")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
