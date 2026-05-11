import json


def test_matrix_multiply_2x2_integers(client):
    body = {"a": [[1, 2], [3, 4]], "b": [[5, 6], [7, 8]]}
    response = client.post(
        "/matrix-multiply",
        data=json.dumps(body),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"result": [[19.0, 22.0], [43.0, 50.0]]}


def test_matrix_multiply_incompatible_shapes(client):
    body = {"a": [[1, 2, 3]], "b": [[1], [2]]}
    response = client.post(
        "/matrix-multiply",
        data=json.dumps(body),
        content_type="application/json",
    )
    assert response.status_code == 400
    assert response.get_json() == {
        "error": "incompatible shapes: columns of a must equal rows of b"
    }


def test_matrix_multiply_ragged_matrix(client):
    body = {"a": [[1, 2], [3]], "b": [[1], [2]]}
    response = client.post(
        "/matrix-multiply",
        data=json.dumps(body),
        content_type="application/json",
    )
    assert response.status_code == 400
    assert response.get_json()["error"] == (
        "a must be rectangular (all rows same length)"
    )
