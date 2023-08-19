from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import HTMLResponse
from pathlib import Path
import requests
from dotenv import load_dotenv
from prometheus_client import Counter, generate_latest

load_dotenv()
from components.constants import DATA_ANALYSIS_BASE_ENDPOINT


BASE_DIR = Path(__file__).resolve().parent
REQUESTS = Counter("app_requests_total", "Total app HTTP requests.")


app = FastAPI()

templates = Jinja2Templates(str(Path(BASE_DIR, "templates")))


@app.get("/")
async def read_root():
    REQUESTS.inc()
    return {"Hello": "World"}


@app.get("/health")
async def health():
    return 200


@app.get("/metrics")
async def metrics():
    return generate_latest()


@app.get("/echo/")
async def read_echo(request: Request, response_class=HTMLResponse):
    REQUESTS.inc()
    return templates.TemplateResponse("input_template.html", {"request": request})


@app.get("/app/")
async def read_app(request: Request, response_class=HTMLResponse):
    REQUESTS.inc()
    return templates.TemplateResponse("app_template.html", {"request": request})


@app.post("/matching-jobs/")
def data_analysis_matching_jobs(
    jobTitle: str = Form(...),
    salary: float = Form(...),
):
    REQUESTS.inc()
    print(f"DA endpoint: {DATA_ANALYSIS_BASE_ENDPOINT}")
    response = requests.get(
        DATA_ANALYSIS_BASE_ENDPOINT
        + f"/matching-jobs?jobTitle={jobTitle}&salary={salary}"
    ).json()
    if not response["matching_jobs"]:
        return 404
    return response["matching_jobs"]


@app.post("/echo/")
async def echo_item(content: str = Form(...)):
    REQUESTS.inc()
    return {"content": content}


if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.getenv("WEB_PORT"))
    host = os.getenv("HOST")

    uvicorn.run(app, host=host, port=port)
