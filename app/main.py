from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# command [ uvicorn main:app --host 0.0.0.0 --reload ]
app = FastAPI()

# CORSの設定
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from routers.analyze_img import analyze_img_router

app.include_router(analyze_img_router)
