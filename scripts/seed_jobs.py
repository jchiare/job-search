import requests
from components.constants import DATA_COLLECTOR_BASE_ENDPOINT


response = requests.get(DATA_COLLECTOR_BASE_ENDPOINT + f"/save-jobs?jobTitle=engineer")
print(response.text)
