serve:
		python manage.py runserver
migrations:
		python manage.py makemigrations
migrate:
		python manage.py migrate
freeze:
		pip freeze > requirements.txt
tests:
		python manage.py test
run:
		heroku run python manage.py migrate
create:
		heroku run python manage.py createsuperuser