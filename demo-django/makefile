run:
	docker compose run --rm web django-admin startproject core .

home:
	docker compose run --rm web python manage.py startapp home

migration:
	docker compose run --rm web python manage.py makemigrations

build:
	docker compose up --build -d

up:
	docker compose up -d

down:
	docker compose down