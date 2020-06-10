# queendb Schema

Migrations for queendb, a database of RuPaul's Drag Race results.

Migrations should include both upgrades and rollbacks.

![Back rolls](https://i.pinimg.com/originals/73/44/64/734464e2fbc27b349c633dbb82ff57cb.gif)

## Dependencies

This project depends on [Poetry](https://python-poetry.org/docs/#installation) as its package manager.

### Install dependencies

        poetry install

## Build Schema

1. Update the `sqlalchemy.url` value in the `alembic.ini` file with your database connection string.

2. Start from base:

        poetry run alembic downgrade base

3. Run all migrations:

        poetry run alembic upgrade head

## Load data

        poetry run python queendb/import.py

## Connecting to the database

TBD

### Downloading and running the Google Cloud SQL Proxy

TBD
