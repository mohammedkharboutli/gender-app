# Name: Makefile

install_dependencies:
	uv sync

start_desktop:
	uv run flet run -r main.py

start_web:
	uv run flet run -r --web --port 8007 main.py

ruff_check:
	uv run ruff check

ruff_check_fix:
	uv run ruff check --fix

ruff_format:
	uv run ruff format

create_uml:
	uv run pyreverse -A -o pdf -p GenderApp controller/GenderAppController.py model/GenderAppModel.py view/GenderAppView.py util/Observable.py util/Observer.py main.py
