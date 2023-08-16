from typing import List
from pydantic import BaseModel
from sqlalchemy import String, and_, func
from components.jobs.dto import ExternalJob
from sqlalchemy.orm import Session, Mapped, mapped_column, declarative_base

Base = declarative_base()


class Jobs(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    applyLink: Mapped[str] = mapped_column(String(255))
    salary: Mapped[float]


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
                func.lower(Jobs.title) == desired_job_title.lower(),
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


def save_jobs_matching_title(db: Session, jobs_response: ExternalJob):
    jobs_array = jobs_response["SearchResult"]["SearchResultItems"]
    count = 0
    for job in jobs_array:
        job = job["MatchedObjectDescriptor"]
        title = job["PositionTitle"]
        applyLink = job["ApplyURI"][0]
        salary = job["PositionRemuneration"][0]["MinimumRange"]
        job_entry = Jobs(title=title, applyLink=applyLink, salary=salary)
        db.add(job_entry)
        count += 1
    db.commit()
    print(f"Added {count} jobs to DB")
