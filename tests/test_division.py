def test_divide_two_integers(client):
    response = client.get("/divide", query_string={"a": 6, "b": 2})
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"quotient": 3.0}


def test_divide_floats(client):
    response = client.get("/divide", query_string={"a": "7.5", "b": "2.5"})
    assert response.status_code == 200
    assert response.get_json() == {"quotient": 3.0}


def test_divide_missing_params(client):
    response = client.get("/divide", query_string={"a": 1})
    assert response.status_code == 400
    assert response.get_json() == {
        "error": "query parameters 'a' and 'b' are required"
    }


def test_divide_non_numeric(client):
    response = client.get("/divide", query_string={"a": "x", "b": 1})
    assert response.status_code == 400
    assert response.get_json()["error"] == "a and b must be numeric"


def test_divide_by_zero(client):
    response = client.get("/divide", query_string={"a": 1, "b": 0})
    assert response.status_code == 400
    assert response.get_json() == {"error": "cannot divide by zero"}
