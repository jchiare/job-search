from typing import List
from pydantic import BaseModel
from sqlalchemy import String, and_, func, Column, Integer, String, Float
from components.jobs.dto import GovernmentJobsApiResponse, SearchResultItem
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()


class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    applyLink = Column(String(255))
    salary = Column(Float)


class JobEntry(BaseModel):
    jobTitle: str
    applyLink: str
    salary: float


def get_matching_jobs_by_salary(
    db: Session, desired_job_title: str, desired_salary: float
) -> List[JobEntry]:
    db_jobs = (
        db.query(Jobs)
        .filter(
            and_(
                func.lower(Jobs.title).ilike(f"%{desired_job_title.lower()}%"),
                Jobs.salary >= desired_salary,
            )
        )
        .all()
    )

    matching_jobs: List[JobEntry] = [
        {
            "jobTitle": job.title,
            "applyLink": job.applyLink,
            "salary": job.salary,
        }
        for job in db_jobs
    ]

    return matching_jobs


def save_jobs_matching_title(db: Session, jobs_response: GovernmentJobsApiResponse):
    jobs_search_results = jobs_response["SearchResult"]["SearchResultItems"]
    jobs_array = parse_related_fields_from_api(jobs_search_results)

    db.add_all(jobs_array)
    db.commit()
    print(f"Added {len(jobs_array)} jobs to DB")


def parse_related_fields_from_api(
    jobs_search_results: List[SearchResultItem],
) -> List[Jobs]:
    jobs = []
    for job in jobs_search_results:
        job = job["MatchedObjectDescriptor"]
        title = job["PositionTitle"]
        apply_link = job["ApplyURI"][0]
        salary = job["PositionRemuneration"][0]["MinimumRange"]
        job_entry = Jobs(title=title, applyLink=apply_link, salary=salary)
        jobs.append(job_entry)
    return jobs
