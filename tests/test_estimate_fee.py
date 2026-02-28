# tests/test_estimate_time.py


def test_estimate_time_returns_status_200(client):
    response = client.get("/estimate-time/12.3")
    assert response.status_code == 200