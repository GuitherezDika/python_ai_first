from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

class LoggerMiddleware(BaseHTTPMiddleware):
    #dispatch = method yang dipanggil setiap ada request, dan wajib 2 parameter
    async def dispatch(self, request: Request, call_next):
        print(f"Request URL: {request.url}")
        response = await call_next(request)
        return response
