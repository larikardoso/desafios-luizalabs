run:
	@uvicorn app.main:app --reload

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m "$(m)"

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head