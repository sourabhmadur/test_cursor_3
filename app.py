from flask import Flask, jsonify, request

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
