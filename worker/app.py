import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )


@app.route("/internal/provision", methods=["POST"])
def internal_provision():
    """Internal endpoint, called by the api service.

    TODO:
    - Read whatever the api service sends you.
    - Create the corresponding schema in Postgres
      (CREATE SCHEMA IF NOT EXISTS ...).
    - Return an appropriate JSON response and status code.
    - Handle errors (e.g. missing input) gracefully.
    """
    raise NotImplementedError


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
