from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import HTMLResponse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

templates = Jinja2Templates(str(Path(BASE_DIR, "templates")))


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/echo/")
async def read_root(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse("input_template.html", {"request": request})


@app.post("/echo/")
async def echo_item(content: str = Form(...)):
    return {"content": content}
