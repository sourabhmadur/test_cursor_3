# test_cursor_3

Small Flask service with a **Hello World** health check, a **sum** endpoint, and a **product** endpoint (both use query parameters `a` and `b` with the same validation rules).

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open [http://127.0.0.1:5000/hello-world](http://127.0.0.1:5000/hello-world). You should see `Hello World`.

### Tests

```bash
pytest
```

## Endpoints

| Method | Path              | Description |
|--------|-------------------|-------------|
| GET    | `/hello-world`    | Health check; body `Hello World` (200). |
| GET    | `/sum?a=&b=`      | JSON `{"sum": <a+b>}`; `a` and `b` must be numeric (400 with JSON error if missing or invalid). |
| GET    | `/product?a=&b=` | JSON `{"product": <a*b>}`; same query parameters and validation as `/sum` (400 with JSON error if missing or invalid). |

Example: [http://127.0.0.1:5000/sum?a=2&b=3](http://127.0.0.1:5000/sum?a=2&b=3) returns `{"sum":5}`.

Example: [http://127.0.0.1:5000/product?a=2&b=3](http://127.0.0.1:5000/product?a=2&b=3) returns `{"product":6}`.

## Requirements

- Python 3.10+

## License

Add a license when you are ready (for example MIT).
