# static dev server with no-cache headers:  python serve.py <dir> <port>
import http.server, sys, functools
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, ".js": "text/javascript", ".webp": "image/webp",
                      ".gltf": "model/gltf+json", ".glb": "model/gltf-binary", ".wasm": "application/wasm"}
http.server.ThreadingHTTPServer(("127.0.0.1", int(sys.argv[2])), functools.partial(H, directory=sys.argv[1])).serve_forever()
