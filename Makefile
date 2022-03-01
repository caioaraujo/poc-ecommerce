run:
	python manage.py migrate && python manage.py runserver

test:
	python -Wa manage.py test

black:
	black .
