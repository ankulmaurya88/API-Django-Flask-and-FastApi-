from fastapi import FastAPI
from core.middleware import JWTMiddleware
from routes import auth, users

app = FastAPI(title="JWT Auth Architecture")

# Middleware
app.add_middleware(JWTMiddleware)

# Routes
app.include_router(auth.router)
app.include_router(users.router)
