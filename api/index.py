import os
import sys
from pathlib import Path

# Add project root directory to sys.path so modules can be imported
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app import app

class VercelPathFixMiddleware:
    """
    Middleware to restore the true request path when Vercel serverless
    rewrites wildcard paths to /api/index.
    """
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        original_uri = (
            environ.get('HTTP_X_FORWARDED_URI') or
            environ.get('HTTP_X_MATCHED_PATH') or
            environ.get('HTTP_X_NOW_ROUTE_MATCHES')
        )
        if original_uri:
            path = original_uri.split('?')[0]
            if path:
                environ['PATH_INFO'] = path
        return self.wsgi_app(environ, start_response)

app.wsgi_app = VercelPathFixMiddleware(app.wsgi_app)

# Vercel entrypoint
handler = app
