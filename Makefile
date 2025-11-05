
all: start

.PHONY: alembic_autogen
alembic_autogen: 
	poetry run alembic revision --autogenerate -m "Initial revision"

.PHONY: alembic_upgrade
alembic_upgrade:
	poetry run alembic upgrade head

.PHONY: docker_start
docker_start:
	bash start_db.sh

.PHONY: flake8
flake8:
	poetry run flake8

.PHONY: start
start: alembic_upgrade
	poetry run uvicorn src.main:app --reload
