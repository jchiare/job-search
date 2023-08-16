import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

print(os.getenv("HOST"))
DATA_ANALYSIS_BASE_ENDPOINT = (
    "http://" + os.getenv("HOST") + ":" + os.getenv("DATA_ANALYSIS_PORT")
)
WEB_BASE_ENDPOINT = "http://" + os.getenv("HOST") + ":" + os.getenv("WEB_PORT")

DATA_COLLECTOR_BASE_ENDPOINT = (
    "http://" + os.getenv("HOST") + ":" + os.getenv("DATA_COLLECTOR_PORT")
)
