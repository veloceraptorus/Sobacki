
.PHONY: alembic_autogen
alembic_autogen: 
	poetry run alembic revision --autogenerate -m "Initial revision"

.PHONY: alembic_upgrade
alembic_upgrade:
	poetry run alembic upgrade head

.PHONY: docker_start
docker_start:
	bash start_db.sh
	sleep 2
	poetry run alembic upgrade head

.PHONY: flake8
flake8:
	poetry run flake8

.PHONY: start
start:
	poetry run uvicorn src.main:app --reload
