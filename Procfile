release: python manage.py migrate --no-input
web: gunicorn saleor.asgi:application -k uvicorn.workers.UvicornWorker
celeryworker: celery -A saleor --app=saleor.celeryconf:app worker --concurrency=2 --loglevel=info -E
