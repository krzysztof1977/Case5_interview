## Scenario

The platform team wants a self-service mechanism for provisioning new
database schemas for product teams, without manual intervention from the
platform team. This environment is a starting point for building that: a
public-facing `api` service, an internal `worker` service, and a Postgres
database — all wired together in `docker-compose.yml`.

```
                 POST /provision
                 {"team_name": "analytics"}
  client  ─────────────────────────────►  api  (public, holds no DB creds)
                                            │
                                            │  ??? (you design this)
                                            ▼
                                          worker  (internal, holds DB creds)
                                            │
                                            │  CREATE SCHEMA IF NOT EXISTS ...
                                            ▼
                                         PostgreSQL
```

- **api** (port 8000): the only service the client talks to. It must not
  hold Postgres credentials itself.
- **worker** (port 8001): the only service with Postgres credentials
  (see its environment variables in `docker-compose.yml`). It performs the
  actual database work.
- **postgres**: the target database.

`docker-compose.yml` is complete and does not need to change. Both services
already have their dependencies (Flask, plus `psycopg2-binary` for worker
and `requests` for api) wired up to install on startup.

## Task

Implement the missing logic in `api/app.py` and `worker/app.py` so that:

1. `POST /provision` on `api`, given `{"team_name": "<name>"}`, results in a
   new Postgres schema being created for that team, and returns a
   confirmation to the client (your choice of exact response shape and
   status code — just make it sensible).
2. `api` never talks to Postgres directly — it must delegate the actual
   database work to `worker` over HTTP. **You design the contract between
   api and worker** (endpoint path, request/response shape).
3. `worker` creates the schema in Postgres (`CREATE SCHEMA IF NOT EXISTS`,
   or equivalent).
4. Basic error handling: a missing `team_name`, and the case where `worker`
   is unreachable or returns an error.

## Running it

```
docker compose up
```

## Testing your solution

```
curl -X POST http://localhost:8000/provision \
  -H "Content-Type: application/json" \
  -d '{"team_name": "analytics"}'
```

Verify the schema was created:

```
docker exec -it postgres psql -U admin -d platform -c "\dn"
```

## Bonus / discussion (not required to implement)

`team_name` comes straight from the client. What could go wrong if it were
used to build a SQL statement naively, and how would you protect against
it?
