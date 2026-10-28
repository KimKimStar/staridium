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
    print("=" * 70)
    print("  🚀 [ViralScope AI] AI 숏폼 바이럴 분석 및 모션 스왑 렌더링 SaaS")
    print(f"  * 접속 주소: {url}")
    print("  * 유튜브 임베드 정책(Error 153 방지)을 위한 HTTP 로컬 서버 가동")
    print("=" * 70)
    
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
            httpd.serve_forever()
    except OSError:
        print(f"포트 {PORT}번이 이미 사용 중입니다. 브라우저에서 {url} 로 접속하세요.")

if __name__ == "__main__":
    main()
