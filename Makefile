SERID=$(shell id -u)
GROUPID=$(shell id -g)

build:
	docker-compose build

test:
	./bin/run.sh pytest .

run:
	docker-compose up

makemigrations:
	./bin/run.sh python manage.py makemigrations

migrate:
	./bin/run.sh python manage.py migrate