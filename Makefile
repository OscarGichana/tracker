serve:
		python manage.py runserver
migration:
		python manage.py makemigrations
migrate:
		python manage.py migrate
freeze:
		pip freeze > requirements.txt
