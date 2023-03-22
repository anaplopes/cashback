.PHONY: prepare
prepare:
	pyenv install 3.10.6
	pyenv local 3.10.6

.PHONY: install
install:
	poetry env use python3.10.6
	poetry install
	poetry run pre-commit install

.PHONY: lint
lint:
	black .
	flake8 .

.PHONY: runserver
runserver:
	uvicorn src.main:create_app --reload

.PHONY: requirements
requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

.PHONY: up
up:
	docker compose --env-file .env up -d --build

.PHONY: down
down:
	docker compose down --remove-orphans -v

.PHONY: clean
clean:
	docker system prune --all --force --volumes
