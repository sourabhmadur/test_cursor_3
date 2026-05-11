def test_hello_world_health_check(client):
    response = client.get("/hello-world")
    assert response.status_code == 200
    assert response.data == b"Hello World"
    assert response.content_type.startswith("text/html")
