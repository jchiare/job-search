import pytest
from components.jobs.db import (
    parse_related_fields_from_api,
    Jobs,
)


@pytest.fixture
def mock_jobs_search_results():
    return [
        {
            "MatchedObjectDescriptor": {
                "PositionTitle": "Software Engineer",
                "ApplyURI": ["https://example.com/apply/se"],
                "PositionRemuneration": [{"MinimumRange": "60000"}],
            }
        },
        {
            "MatchedObjectDescriptor": {
                "PositionTitle": "Data Scientist",
                "ApplyURI": ["https://example.com/apply/ds"],
                "PositionRemuneration": [{"MinimumRange": "80000"}],
            }
        },
    ]


def test_parse_related_fields_from_api(mock_jobs_search_results):
    result = parse_related_fields_from_api(mock_jobs_search_results)

    expected = [
        Jobs(
            title="Software Engineer",
            applyLink="https://example.com/apply/se",
            salary="60000",
        ),
        Jobs(
            title="Data Scientist",
            applyLink="https://example.com/apply/ds",
            salary="80000",
        ),
    ]

    assert len(result) == len(expected), "Mismatch in number of parsed jobs"

    for r, e in zip(result, expected):
        assert r.title == e.title, f"Expected title {e.title}, but got {r.title}"
        assert (
            r.applyLink == e.applyLink
        ), f"Expected applyLink {e.applyLink}, but got {r.applyLink}"
        assert r.salary == e.salary, f"Expected salary {e.salary}, but got {r.salary}"
