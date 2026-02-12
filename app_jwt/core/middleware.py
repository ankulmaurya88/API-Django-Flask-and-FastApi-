from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from core.security import verify_token


class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth_header = request.headers.get("Authorization")

        if auth_header:
            scheme, _, token = auth_header.partition(" ")

            if scheme.lower() == "bearer":
                payload = verify_token(token)

                if not payload or payload.get("type") != "access":
                    raise HTTPException(status_code=401, detail="Invalid or expired token")

                # Attach user context
                request.state.user = payload

        response = await call_next(request)
        return response
