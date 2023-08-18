from fastapi import FastAPI, HTTPException, Depends, Query
from components.jobs import external
from components.jobs.db import save_jobs_matching_title
from sqlalchemy.orm import Session
from components.database import get_db

app = FastAPI()


@app.get("/save-jobs")
def find_jobs(
    jobTitle: str = Query(...),
    db: Session = Depends(get_db),
):
    jobs = external.fetch_jobs_from_gov(jobTitle)
    if jobs["SearchResult"]["SearchResultCountAll"] == 0:
        raise HTTPException(status_code=404, detail="No jobs found")
    save_jobs_matching_title(db, jobs)
    return 200


if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.getenv("DATA_COLLECTOR_PORT"))

    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
