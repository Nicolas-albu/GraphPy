install:
	@poetry install
format:
	@black .
	@isort .
lint:
	@black --check .
	@isort --check .
test:
	@pytest tests/ -v