def test_sum_two_integers(client):
    response = client.get("/sum", query_string={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"sum": 5}


def test_sum_floats(client):
    response = client.get("/sum", query_string={"a": "1.5", "b": "2.5"})
    assert response.status_code == 200
    assert response.get_json() == {"sum": 4.0}


def test_sum_missing_params(client):
    response = client.get("/sum", query_string={"a": 1})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_sum_non_numeric(client):
    response = client.get("/sum", query_string={"a": "x", "b": 1})
    assert response.status_code == 400
    assert response.get_json()["error"] == "a and b must be numeric"
