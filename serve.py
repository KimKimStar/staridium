import http.server
import socketserver
import os
import sys

# Windows CP949 콘솔 인코딩 충돌 방지
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

PORT = 8500
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.path = "/index.html"
        return super().do_GET()

def main():
    os.chdir(DIRECTORY)
    url = f"http://127.0.0.1:{PORT}/index.html"
    print("=" * 65)
    print("  [ViralScope AI] YouTube Shorts Real-Time Viral SaaS Dashboard")
    print(f"  * URL: {url}")
    print("  * YouTube Error 153 Prevented: HTTP Origin Active")
    print("=" * 65)
    
    # 포트 재사용 허용
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
            httpd.serve_forever()
    except OSError as e:
        # Port already in use, which is fine (server already running)
        print(f"Server already listening on port {PORT}.")

if __name__ == "__main__":
    main()
