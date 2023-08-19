## Job Search Application

Web application with two backend services that fetch US government jobs, analysis the fetched jobs to parse matching ones with a given title, and sends the relevant jobs found to the web app user.

## CU - Boulder Class

Answer to Week 3 - Data Collection: 

- [x] Fetch Data from external source: Done in the data_collector app on the endpoint `save-jobs`, using the function `fetch_jobs_from_gov` from the file `components/jobs/external.py`. The data fetching is scheduled using cron in production.
- [x] Store data in the database: Saves jobs with matching title to a MySQL (cloud hosted on PlanetScale) database, using the function `save_jobs_matching_title` from the file `components/jobs/db.py`

Answer to Week 3 - Data Analysis: 

- [x] Retrieves data from database: Done in the data_analysis app on the endpoint `matching-jobs`, using the function `get_matching_jobs_by_salary` from the file `components/jobs/db.py`.
- [x] Perform analysis: Analysis of relevant jobs is performed on the same endpoint and same function as the above. We analyze jobs based on what the user wants in terms of salary and job title 
- [x] Should be ran as a standalone process / server using the command `python applications/data_analysis/app.py`. Can also run a script using cron in production with command `python scripts/analyze_jobs.py` 

Answer to Week 2:

- Unit test: `/tests/components/jobs/db_unit_test.py` -> test_parse_related_fields_from_api function
- Integration test: `/tests/applications/data_analysis/main_integration_test.py` -> test_parse_related_fields_from_api function
- CI/CD: `.github/workflows/deploy.yml`

## Database details

* MySQL database using SQLalchemy as the ORM
* Hosted in the cloud using [PlanetScale](https://planetscale.com)

## CI/CD details

* For CI, we use github actions (as seen in the `test` job in the github workflow) to test all changes to the `main` branch
* For CD, we use [Dokku](https://dokku.com/), an open source PaaS like heroku that makes it easy to deploy the code changes to a remote server
* I host the server on a VM on [Hetzner](https://www.hetzner.com/)

## Install dependencies

Tested with Python `3.10.5`

1. Start the virtual environment with `source env/bin/activate`
2. Install requirements with `pip install -r requirements.txt`
3. Get the environment variables (some are secret so won't be in zip)

## How to test

1. Install dependencies
2. Run `pytest`

## How to run servers

- Data Collector process: `python applications/data_collector/app.py`
- Data Analysis process: `python applications/data_analysis/app.py`
- Web App process: `python applications/web/app.py`

Note: When deploying to production using Dokku, Dokku first builds the dockerfile then runs starts each process with commands defined in `Procfile`
