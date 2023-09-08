import requests
import os

from components.jobs.dto import GovernmentJobsApiResponse


def fetch_jobs_from_gov(title: str) -> GovernmentJobsApiResponse:
    url = "https://data.usajobs.gov/api/search?Keyword=" + title
    headers = {
        "User-Agent": os.environ.get("GOV_JOBS_EMAIL"),
        "Host": "data.usajobs.gov",
        "Authorization-Key": os.environ.get("GOV_JOBS_API_KEY"),
    }
    print(url)

    response = requests.get(url, headers=headers)
    return response.json()
