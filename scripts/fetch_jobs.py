import requests
from components.constants import DATA_COLLECTOR_BASE_ENDPOINT
import sys

response = requests.get(
    DATA_COLLECTOR_BASE_ENDPOINT + f"/save-jobs?jobTitle={sys.argv[1]}"
)
print(response.text)
