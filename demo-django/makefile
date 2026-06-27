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

create_user:
	docker compose exec web python manage.py createsuperuser

db_migrate:
	docker compose run --rm web python manage.py migrate