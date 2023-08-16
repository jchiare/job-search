import requests
import os

from components.jobs.dto import ExternalJob


def fetch_jobs(title: str) -> ExternalJob:
    url = "https://data.usajobs.gov/api/search?Keyword=" + title
    headers = {
        "User-Agent": os.environ.get("GOV_JOBS_EMAIL"),
        "Host": "data.usajobs.gov",
        "Authorization-Key": os.environ.get("GOV_JOBS_API_KEY"),
    }

    response = requests.get(url, headers=headers)
    return response.json()
