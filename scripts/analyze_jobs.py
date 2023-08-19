import requests
from components.constants import DATA_ANALYSIS_BASE_ENDPOINT
import sys

response = requests.get(
    DATA_ANALYSIS_BASE_ENDPOINT
    + f"/matching-jobs?jobTitle={sys.argv[0]}&salary={sys.argv[1]}"
)
print(response.text)
