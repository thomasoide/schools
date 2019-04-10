.PHONY: env

env:
	echo 'DJANGO_SECRET_KEY=dev123' >> .env
	echo 'DATABASE_URL=psql://'`whoami`':@127.0.0.1:5432/schools' >> .env
	echo 'DEBUG=True' >> .env

syncdb:
	dropdb schools
	createdb schools
	rm -rf schools/district_search/migrations
	python manage.py makemigrations district_search
	python manage.py migrate
