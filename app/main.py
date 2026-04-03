from flask import (
    Flask,
    jsonify,
    Response
)

from http import HTTPStatus

app = Flask(__name__)

@app.route("/")
def home() -> Response:
    return jsonify(
        {
            "message": "Aqui é a rota inicial."
        }
    ), HTTPStatus.OK

@app.route("/health")
def health() -> Response:
    return jsonify(
        {
            "status": "OK"
        }
    ), HTTPStatus.OK

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5687,
        debug=False
    )
