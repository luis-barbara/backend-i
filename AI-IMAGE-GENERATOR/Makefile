start:
	poetry run python manage.py runserver

migrate:
	docker compose run --rm web poetry run python manage.py migrate

migrations:
	docker compose run --rm web poetry run python manage.py makemigrations
	@# se eliminar pasta 

createsuperuser:
	poetry run python manage.py createsuperuser

new-app:
	poetry run python manage.py startapp $(app)
	@# to execute run "make new-app app=cenas"

pyclean:
	pyclean .

tests:
	poetry run pytest -vvv

compose.migrate:
	docker compose run --rm web poetry run python manage.py migrate