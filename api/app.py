import os
from flask import Flask, request, jsonify

app = Flask(__name__)

WORKER_URL = os.environ["WORKER_URL"]


@app.route("/provision", methods=["POST"])
def provision():
    """Public-facing self-service endpoint.

    TODO:
    - Read "team_name" from the JSON request body.
    - Derive a schema name from it.
    - Call the worker service so it creates the schema in Postgres
      (design the request/response contract between api and worker
      yourself).
    - Return the created schema name with an appropriate status code.
    - Handle missing "team_name" and an unreachable worker gracefully.
    """
    raise NotImplementedError


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
