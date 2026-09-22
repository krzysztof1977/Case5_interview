import os
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_connection():
    """TODO: connect to Postgres using psycopg2.

    Connection details are provided via the DB_HOST, DB_NAME, DB_USER and
    DB_PASSWORD environment variables (see docker-compose.yml).
    """
    raise NotImplementedError


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
