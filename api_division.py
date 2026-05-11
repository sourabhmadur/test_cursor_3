from flask import Flask, jsonify, request


def register_division_routes(app: Flask) -> None:
    """Register GET /divide: quotient of query parameters ``a`` and ``b``."""

    @app.route("/divide")
    def divide_numbers():
        a_raw = request.args.get("a")
        b_raw = request.args.get("b")
        if a_raw is None or b_raw is None:
            return jsonify(error="query parameters 'a' and 'b' are required"), 400
        try:
            a = float(a_raw)
            b = float(b_raw)
        except ValueError:
            return jsonify(error="a and b must be numeric"), 400
        if b == 0:
            return jsonify(error="cannot divide by zero"), 400
        return jsonify(quotient=a / b)
