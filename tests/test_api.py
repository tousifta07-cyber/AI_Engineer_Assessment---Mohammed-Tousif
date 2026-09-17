from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_query():
    response = client.post(
        "/query",
        json={
            "question": "How many critical tickets are there?"
        }
    )

    assert response.status_code == 200
    assert response.json()["answer"] == 55


def test_anomalies():
    response = client.get("/anomalies")

    assert response.status_code == 200
    assert "count" in response.json()
    assert "anomalies" in response.json()


def test_critical_unresolved():
    response = client.post(
        "/query",
        json={
            "question": "How many critical tickets are unresolved?"
        }
    )

    assert response.status_code == 200
    assert isinstance(response.json()["answer"], int)


def test_lowest_agent_rating():
    response = client.post(
        "/query",
        json={
            "question": "Which agent has the lowest average customer rating?"
        }
    )

    assert response.status_code == 200
    assert isinstance(response.json()["answer"], str)