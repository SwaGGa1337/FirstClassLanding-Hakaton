.PHONY: run-server clean install docker

run-server:
	@echo "Starting server..."
	@python backend/manage.py runserver

install:
	@echo "Installing dep..."
	@pip install poetry
	@poetry shell
	@poetry install
	@poetry update
	@sudo apt-get update
	@poetry lock

clean:
	@echo "Removing lock..."
	@rm poetry.lock

docker: 
	@sudo docker-compose up --build -d