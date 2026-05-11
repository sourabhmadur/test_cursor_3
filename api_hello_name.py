from flask import Flask, jsonify, request


def register_hello_name_routes(app: Flask) -> None:
    """Register GET /hello_name: returns a personalized hello string."""

    @app.route("/hello_name")
    def hello_name():
        name = request.args.get("name")
        if name is None or name.strip() == "":
            return jsonify(error="query parameter 'name' is required"), 400
        return f"hello_{name}", 200
