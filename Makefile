SHELL := /bin/bash
.DEFAULT_GOAL := help

.PHONY: help install-dev install-venv create-venv activate-venv \
		build up down up-d down-v kill\
		logs tests lint format clean \
		migrate createsuperuser collectstatic shell \
		createsuperuser makemigrations

# Variables
ACCEPTABLE_SERVICES := web worker beat db
SERVICE ?= web
CURRENT_DIR := $(shell pwd)
COMPOSE_FILE := devops/docker-compose.local.yml
COMPOSE_PROJECT := console
COMPOSE_COMMAND := docker-compose -f $(COMPOSE_FILE) -p $(COMPOSE_PROJECT)

# Targets
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "requirements			to create a virtual environment and install python packages inside of it."
	@echo "build	    			to build the project by running the 'docker-compose build' command."
	@echo "up	    			to start the development environment by running the 'docker-compose up' command."
	@echo "up-d	    			to start the development environment in detached mode by running the 'docker-compose up -d' command"
	@echo "down	    			to stop the development environment by running the 'docker-compose down' command."
	@echo "down-v				to stop the development environment and remove the volumes by running the 'docker-compose down' command."
	@echo "kill	    			to stop the development environment by running the 'docker-compose down' command."
	@echo "reboot	    		to restart the development environment"
	@echo "logs	    			to show container's logs with -f flag"
	@echo "tests     			to run the test suite"
	@echo "lint      			to run the flake8 command and check linting"
	@echo "format    			to run the black command and format the code"
	@echo "clean     			to remove temporary files and directories"
	@echo "makemigrations			to create new database migrations"
	@echo "migrate				to apply database migrations"
	@echo "createsuperuser			to create a superuser"
	@echo "collectstatic			to collect static files"
	@echo "shell				to open a Django shell"

install-venv:
	sudo apt install virtualenv

create-venv:
	virtualenv -p python3 .venv

requirements: install-venv create-venv
	source $(CURRENT_DIR)/.venv/bin/activate && pip install -r requirements/local.txt

build:
	$(COMPOSE_COMMAND) build

up:
	$(COMPOSE_COMMAND) up --remove-orphans

up-d:
	$(COMPOSE_COMMAND) up -d --remove-orphans

down:
	$(COMPOSE_COMMAND) down

down-v:
	$(COMPOSE_COMMAND) down -v

kill:
	$(COMPOSE_COMMAND) kill

reboot:
	$(COMPOSE_COMMAND) kill && $(COMPOSE_COMMAND) up --remove-orphans

logs:
	$(COMPOSE_COMMAND) logs -f

define MANAGE_COMMAND
	@SERVICE_NAME=$(filter-out $@,$(MAKECMDGOALS)); \
	if [ -z "$$SERVICE_NAME" ]; then \
		SERVICE_NAME=$(SERVICE); \
	fi; \
	if echo $(ACCEPTABLE_SERVICES) | grep -q -w $$SERVICE_NAME; then \
		if [ $@ == exec ]; then \
			$(COMPOSE_COMMAND) exec $$SERVICE_NAME /bin/bash; \
		else \
			$(COMPOSE_COMMAND) exec $$SERVICE_NAME python manage.py $@; \
		fi; \
	else \
		echo "Invalid service name. Acceptable service names are: $(ACCEPTABLE_SERVICES)"; \
		exit 1; \
	fi
endef

shell makemigrations migrate collectstatic createsuperuser test exec:
	$(MANAGE_COMMAND)

%:
	@:

lint:
	flake8

format:
	isort --profile black .
	black .

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
