import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def da_base_url():
    return (
        os.getenv("HOST")
        if os.getenv("ENV") == "local"
        else "job-search.dataanalysis.1"
    )


def dc_base_url():
    return (
        os.getenv("HOST")
        if os.getenv("ENV") == "local"
        else "job-search.datacollector.1"
    )


DATA_ANALYSIS_BASE_ENDPOINT = (
    "http://" + da_base_url() + ":" + os.getenv("DATA_ANALYSIS_PORT")
)
WEB_BASE_ENDPOINT = "http://" + os.getenv("HOST") + ":" + os.getenv("WEB_PORT")

DATA_COLLECTOR_BASE_ENDPOINT = (
    "http://" + dc_base_url() + ":" + os.getenv("DATA_COLLECTOR_PORT")
)
