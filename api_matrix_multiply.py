import json

from flask import Flask, jsonify, request


def _is_number(x: object) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _validate_matrix(m: object, name: str) -> str | None:
    if not isinstance(m, list):
        return f"{name} must be a list of rows"
    if len(m) == 0:
        return f"{name} must be a non-empty list of rows"
    row_len: int | None = None
    for row in m:
        if not isinstance(row, list):
            return f"{name} rows must be lists"
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            return f"{name} must be rectangular (all rows same length)"
        for x in row:
            if not _is_number(x):
                return f"{name} entries must be numbers (int or float)"
    return None


def _matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    rows_a = len(a)
    cols_a = len(a[0]) if rows_a else 0
    rows_b = len(b)
    cols_b = len(b[0]) if rows_b else 0
    result: list[list[float]] = []
    for i in range(rows_a):
        row_out: list[float] = []
        for j in range(cols_b):
            s = 0.0
            for k in range(cols_a):
                s += a[i][k] * b[k][j]
            row_out.append(s)
        result.append(row_out)
    return result


def register_matrix_multiply_routes(app: Flask) -> None:
    """Register POST /matrix-multiply: JSON body ``{"a": matrix, "b": matrix}``."""

    @app.route("/matrix-multiply", methods=["POST"])
    def matrix_multiply():
        if not request.is_json:
            return jsonify(error="content-type must be application/json"), 400
        raw = request.get_data(cache=True)
        if not raw or not raw.strip():
            return jsonify(error="empty body"), 400

        try:
            data = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            return jsonify(error="invalid json"), 400
        if not isinstance(data, dict):
            return jsonify(error="body must be a json object"), 400
        if "a" not in data or "b" not in data:
            return jsonify(error="body must include keys 'a' and 'b'"), 400

        err = _validate_matrix(data["a"], "a")
        if err:
            return jsonify(error=err), 400
        err = _validate_matrix(data["b"], "b")
        if err:
            return jsonify(error=err), 400

        a = data["a"]
        b = data["b"]
        cols_a = len(a[0]) if a else 0
        rows_b = len(b)

        if cols_a != rows_b:
            return (
                jsonify(
                    error="incompatible shapes: columns of a must equal rows of b"
                ),
                400,
            )

        # Coerce to float for consistent arithmetic (e.g. int * int).
        af: list[list[float]] = [[float(x) for x in row] for row in a]
        bf: list[list[float]] = [[float(x) for x in row] for row in b]
        result = _matmul(af, bf)
        return jsonify(result=result)
