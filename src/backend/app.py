from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
app = FastAPI()
target_dir = "../frontend"
app.mount("/", StaticFiles(directory=target_dir, html=True), name="site")