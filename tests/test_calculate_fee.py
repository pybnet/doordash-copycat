# tests/test_calculate_fee.py


def test_calculate_fee_valid_payload(client):
    payload = {
        "distance_km": 10.5,
        "weight_kg": 2.0,
    }
    response = client.post("/calculate-fee/", json=payload)
    assert response.status_code == 200