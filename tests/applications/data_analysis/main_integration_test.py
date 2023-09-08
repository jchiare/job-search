from fastapi.testclient import TestClient
import pytest
from sqlalchemy.orm import sessionmaker
from components.database import create_db_engine
from applications.data_analysis.app import app
from components.jobs.db import Jobs


client = TestClient(app)


@pytest.fixture(scope="function")
def test_db():
    engine = create_db_engine()
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    db = SessionLocal()
    yield db

    db.query(Jobs).filter(Jobs.applyLink.like("http://test%")).delete()
    db.commit()
    db.close()


def test_matching_jobs(test_db):
    job1 = Jobs(title="Engineer", applyLink="http://test.com", salary=50000.0)
    job2 = Jobs(title="Engineer", applyLink="http://test2.com", salary=70000.0)
    job3 = Jobs(title="Doctor", applyLink="http://test3.com", salary=100000.0)
    test_db.add(job1)
    test_db.add(job2)
    test_db.add(job3)
    test_db.commit()

    response = client.get(
        "/matching-jobs", params={"jobTitle": "Engineer", "salary": 55000.0}
    )

    expected_response = {
        "matching_jobs": [
            {"jobTitle": "Engineer", "applyLink": "http://test2.com", "salary": 70000.0}
        ]
    }
    assert response.status_code == 200
    assert response.json() == expected_response
