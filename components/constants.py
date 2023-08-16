import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

for key, value in os.environ.items():
    if not key.startswith("GOV_"):
        print(f"{key}={value}")

import pwd

user_id = os.getuid()
user_info = pwd.getpwuid(user_id)
print(user_info.pw_name)

with open(os.path.expanduser("~/.bashrc"), "r") as file:
    content = file.read()
    print(content)
DATA_ANALYSIS_BASE_ENDPOINT = (
    "http://" + os.getenv("HOST") + ":" + os.getenv("DATA_ANALYSIS_PORT")
)
WEB_BASE_ENDPOINT = "http://" + os.getenv("HOST") + ":" + os.getenv("WEB_PORT")

DATA_COLLECTOR_BASE_ENDPOINT = (
    "http://" + os.getenv("HOST") + ":" + os.getenv("DATA_COLLECTOR_PORT")
)
