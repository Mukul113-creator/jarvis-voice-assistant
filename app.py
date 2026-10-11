"""Web version of Jarvis: serves the page and a small JSON API.

Run locally:   python app.py        then open http://127.0.0.1:5000
Deploy:        gunicorn app:app
"""
from flask import Flask, jsonify, request, send_from_directory

from jarvis_core import process

app = Flask(__name__, static_folder="static", static_url_path="/static")


@app.get("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


@app.post("/api/command")
def command():
    data = request.get_json(silent=True) or {}
    text = str(data.get("text", ""))[:500]
    tz = data.get("tz")
    return jsonify(process(text, tz if isinstance(tz, str) else None))


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(debug=True)
