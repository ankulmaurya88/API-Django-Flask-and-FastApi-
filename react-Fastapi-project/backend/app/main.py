from fastapi import FastAPI
from app.database import Base, engine
from app.routes import note

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Public Notes API")

app.include_router(note.router)



# if __name__ == "__main__":
#     uvicorn.run(
#         "app.main:app",
#         host="0.0.0.0",
#         port=8000,
#         reload=True
#     )