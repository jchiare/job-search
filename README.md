Answer to Week 2:

- Unit test: `/tests/components/jobs/db_unit_test.py` -> test_parse_related_fields_from_api function
- Integration test: `/tests/applications/data_analysis/main_integration_test.py` -> test_parse_related_fields_from_api function
- CI/CD: `.github/workflows/deploy.yml`

## CI/CD details

* For CI, we use github actions (as seen in the `test` job in the github workflow) to test all changes to the `main` branch
* For CD, we use [Dokku](https://dokku.com/), an open source PaaS like heroku that makes it easy to deploy the code changes to a remote server
* I host the server on a VM on [Hetzner](https://www.hetzner.com/)

## How to test

Tested with Python `3.10.5`

1. Start the virtual environment with `source env/bin/activate`
2. Install requirements with `pip install -r requirements.txt`
3. Get the environment variables (some are secret so won't be in zip)
4. Run `pytest`