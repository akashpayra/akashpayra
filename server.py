import http.server
import socketserver
import json

PORT = 8080

class DeveloperProfileServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Return developer system initialization log
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        status_payload = {
            "status": "online",
            "environment": "production",
            "developer": "akashpayra",
            "modules_loaded": ["vs-code", "git-core", "terminal-ui"],
            "system_latency": "0.04ms"
        }
        
        self.wfile.write(bytes(json.dumps(status_payload, indent=4), "utf-8"))

if __name__ == "__main__":
    print(f"[SUCCESS] Akash's Local Environment Online at http://localhost:{PORT}")
    with socketserver.TCPServer(("", PORT), DeveloperProfileServer) as httpd:
        httpd.serve_forever()
