#!/usr/bin/env bash
# Render build: install deps, collect static files, migrate, create grader accounts.
# Needs DATABASE_URL and SECRET_KEY in the environment. Run: ./build.sh
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py seed
