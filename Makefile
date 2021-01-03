run:
	python manage.py migrate && python manage.py runserver

test:
	python manage.py test