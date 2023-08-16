import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DATA_ANALYSIS_BASE_ENDPOINT = (
    "http://" + "job-search.dataanalysis.1" + ":" + os.getenv("DATA_ANALYSIS_PORT")
)
WEB_BASE_ENDPOINT = "http://" + os.getenv("HOST") + ":" + os.getenv("WEB_PORT")

DATA_COLLECTOR_BASE_ENDPOINT = (
    "http://" + "job-search.datacollector.1" + ":" + os.getenv("DATA_COLLECTOR_PORT")
)
