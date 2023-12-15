# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

all: down build up test

build:
	docker-compose build

up:
	docker-compose up -d app

down:
	docker-compose down --remove-orphans

ps:
	docker-compose ps

test: up
	docker-compose run --rm --no-deps --entrypoint=pytest app /tests/unit /tests/integration /tests/e2e

unit:
	docker-compose run --rm --no-deps --entrypoint=pytest app /tests/unit

integration: up
	docker-compose run --rm --no-deps --entrypoint=pytest app /tests/integration

e2e: up
	docker-compose run --rm --no-deps --entrypoint=pytest app /tests/e2e

logs:
	docker-compose logs app | tail -100

black:
	black -l 86 $$(find * -name '*.py')
