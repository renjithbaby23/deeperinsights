.PHONY: notebook docs
.EXPORT_ALL_VARIABLES:

install:
	@echo "setting up virtual environment..."
	poetry install
	poetry run pre-commit install

	@echo "building solution package..."
	poetry build

	@echo "installing the solution package..."
	pip install dist/solution-0.1.0-py3-none-any.whl --force-reinstall

activate:
	@echo "Activating virtual environment"
	poetry shell

initialize_git:
	git init

pull_data:
	poetry run dvc pull

setup: initialize_git install

test:
	pytest

docs_view:
	@echo View API documentation...
	pdoc src --http localhost:8080

docs_save:
	@echo Save documentation to docs...
	pdoc src -o docs

pre_commit:
	@echo Running pre-commit run --all-files...
	pre-commit run --all-files

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .mypy_cache
	rm -rf .pytest_cache
