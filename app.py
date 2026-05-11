from flask import Flask, jsonify, request

from api_division import register_division_routes
from api_hello_name import register_hello_name_routes
from api_matrix_multiply import register_matrix_multiply_routes

app = Flask(__name__)


@app.route("/hello-world")
def hello_world():
    """Health check: returns plain text OK response."""
    return "Hello World", 200


@app.route("/sum")
def sum_numbers():
    """Return the sum of two numbers passed as query parameters ``a`` and ``b``."""
    a_raw = request.args.get("a")
    b_raw = request.args.get("b")
    if a_raw is None or b_raw is None:
        return jsonify(error="query parameters 'a' and 'b' are required"), 400
    try:
        a = float(a_raw)
        b = float(b_raw)
    except ValueError:
        return jsonify(error="a and b must be numeric"), 400
    return jsonify(sum=a + b)


@app.route("/product")
def product_numbers():
    """Return the product of two numbers passed as query parameters ``a`` and ``b``."""
    a_raw = request.args.get("a")
    b_raw = request.args.get("b")
    if a_raw is None or b_raw is None:
        return jsonify(error="query parameters 'a' and 'b' are required"), 400
    try:
        a = float(a_raw)
        b = float(b_raw)
    except ValueError:
        return jsonify(error="a and b must be numeric"), 400
    return jsonify(product=a * b)


register_division_routes(app)
register_matrix_multiply_routes(app)
register_hello_name_routes(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
