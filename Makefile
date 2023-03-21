.PHONY: prepare
prepare:
	pyenv install 3.10.6
	pyenv local 3.10.6

.PHONY: install
install:
	poetry install

.PHONY: runserver
runserver:
	uvicorn cashback.main:app --reload

.PHONY: requirements
requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

.PHONY: up
up:
	docker compose up -d --build

.PHONY: down
down:
	docker compose down --remove-orphans -v

.PHONY: clean
clean:
	docker system prune --all --force --volumes
