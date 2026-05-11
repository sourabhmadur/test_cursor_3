def test_hello_name_success(client):
    response = client.get("/hello_name", query_string={"name": "Ada"})
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "hello_Ada"


def test_hello_name_missing(client):
    response = client.get("/hello_name")
    assert response.status_code == 400
    assert response.get_json() == {"error": "query parameter 'name' is required"}


def test_hello_name_blank(client):
    response = client.get("/hello_name", query_string={"name": "   "})
    assert response.status_code == 400
    assert response.get_json() == {"error": "query parameter 'name' is required"}
