from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
SITE_DIR = BASE_DIR / "site"

app = FastAPI(title="HNKSTORE Web/API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/assets", StaticFiles(directory=SITE_DIR / "assets"), name="assets")

@app.get("/api/health")
def health():
    return {"ok": True, "service": "HNKSTORE Web/API", "stage": "project-2-base"}

@app.get("/")
def home():
    return FileResponse(SITE_DIR / "index.html")

@app.get("/admin")
def admin():
    return FileResponse(SITE_DIR / "admin.html")
