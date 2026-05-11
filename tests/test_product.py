def test_product_two_integers(client):
    response = client.get("/product", query_string={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"product": 6}


def test_product_floats(client):
    response = client.get("/product", query_string={"a": "1.5", "b": "2.5"})
    assert response.status_code == 200
    assert response.get_json() == {"product": 3.75}


def test_product_missing_params(client):
    response = client.get("/product", query_string={"a": 1})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_product_non_numeric(client):
    response = client.get("/product", query_string={"a": "x", "b": 1})
    assert response.status_code == 400
    assert response.get_json()["error"] == "a and b must be numeric"
