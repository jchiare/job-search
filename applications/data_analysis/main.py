from components.database.db import get_db
from fastapi import FastAPI, Query, Depends
from sqlalchemy.orm import Session
from components.jobs.db import get_matching_jobs_by_salary
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/matching-jobs")
async def submit_info(
    jobTitle: str = Query(...),
    salary: float = Query(...),
    db: Session = Depends(get_db),
):
    matching_jobs = get_matching_jobs_by_salary(db, jobTitle, salary)

    print(matching_jobs)
    return {"matching_jobs": matching_jobs}


if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.getenv("DATA_ANALYSIS_PORT"))
    host = os.getenv("HOST")

    uvicorn.run("main:app", host=host, port=port, reload=True)
