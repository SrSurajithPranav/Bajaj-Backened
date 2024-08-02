import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# User details
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/bfhl':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            request_data = json.loads(post_data)

            numbers = []
            alphabets = []
            highest_alphabet = []

            for item in request_data.get('data', []):
                if item.isdigit():
                    numbers.append(item)
                elif item.isalpha() and len(item) == 1:
                    alphabets.append(item)

            if alphabets:
                highest_alphabet_char = max(alphabets, key=lambda x: x.upper())
                highest_alphabet.append(highest_alphabet_char)

            response_data = {
                "is_success": True,
                "user_id": USER_ID,
                "email": EMAIL,
                "roll_number": ROLL_NUMBER,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet,
            }

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def do_GET(self):
        if self.path == '/bfhl':
            response_data = {
                "operation_code": 1
            }

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
