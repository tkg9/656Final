# 656Final

StageCraft, a backstage assistant for theatre stage managers and crews.
MGT 656 (Fall 2026) final project, team daunting-horizon.

- [Project proposal](docs/proposal.md)
- [User stories](docs/user-stories.md)
- [Progress log](PROGRESS.md)

## Run locally

```sh
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed        # grader accounts
python manage.py runserver   # http://127.0.0.1:8000
```

Without `DATABASE_URL` the app uses a local SQLite file; staging uses Postgres.

## Test

```sh
python manage.py test
```

CI on pull requests is planned.

## Workflow

Branch, pull request, one teammate's review, merge. No direct pushes to `main`.
