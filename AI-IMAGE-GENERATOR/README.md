- superuser: dali/admin@123
- user: johncenas/aluno123
- user: mariamu/eticalgarve123
- poetry add python-dotenv
- poetry add openai


# CLI with Typer

## List commands
docker compose run --rm web poetry run python cli_typer.py --help

## List characters
docker compose run --rm -e DJANGO_SETTINGS_MODULE=dali.settings web poetry run python cli_typer.py list-characters

## Delete character
docker compose run --rm -e DJANGO_SETTINGS_MODULE=dali.settings web poetry run python cli_typer.py delete-character 1

## Show stats
docker compose run --rm -e DJANGO_SETTINGS_MODULE=dali.settings web poetry run python cli_typer.py character-stats

## Run development server
docker compose run --rm -e DJANGO_SETTINGS_MODULE=dali.settings web poetry run python cli_typer.py runserver







# AI Image Generator

## Project Overview

The **AI Image Generator** is a Django-based web application that generates and manages characters using machine learning models and AI services. This project is designed to provide an interface for creating, listing, deleting, and displaying statistics of generated characters. It includes a command-line interface (CLI) for various operations and is Dockerized for easy deployment.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
  - [Environment Setup](#environment-setup)
  - [Docker Setup](#docker-setup)
- [Usage](#usage)
  - [Run Django Development Server](#run-django-development-server)
  - [CLI Commands](#cli-commands)
- [Testing](#testing)
- [Makefile Commands](#makefile-commands)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Character Generation**: Create AI-generated characters.
- **Character Management**: List and delete generated characters.
- **Statistics**: View statistics about the generated characters.
- **Django Admin**: Create superusers and manage the application through Django's admin interface.
- **Docker Support**: Run the application and all dependencies in Docker containers for easier development and deployment.
- **CLI Interface**: Perform various operations through a command-line interface.

## Installation

### Prerequisites

- **Docker**: Make sure Docker and Docker Compose are installed on your machine. You can install them from the official Docker documentation:
  - [Install Docker](https://docs.docker.com/get-docker/)
  - [Install Docker Compose](https://docs.docker.com/compose/install/)

- **Poetry**: Poetry is used for dependency management. Install it by following the instructions here:
  - [Poetry Installation](https://python-poetry.org/docs/#installation)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ai-image-generator.git
   cd ai-image-generator
   ```

2. **Install Dependencies**:
   - Install Python dependencies using Poetry:
     ```bash
     poetry install
     ```

3. **Set up the Environment Variables**:
   - Create a `.env` file and set your `DJANGO_SETTINGS_MODULE` to point to the correct settings file:
     ```bash
     DJANGO_SETTINGS_MODULE=dali.settings
     ```

4. **Configure Docker**:
   - The project uses Docker Compose to handle the database and other services. The `docker-compose.yml` file is included.
   - Build and start the services:
     ```bash
     docker-compose up --build
     ```

5. **Database Migration**:
   - After starting the Docker containers, you need to apply migrations:
     ```bash
     docker-compose run --rm web poetry run python manage.py migrate
     ```

6. **Create a Superuser**:
   - Once the database is set up, create a superuser to access the Django admin:
     ```bash
     docker-compose run --rm web poetry run python manage.py createsuperuser
     ```

## Setup

### Environment Setup
Set up the required environment variable `DJANGO_SETTINGS_MODULE`. You can set it either in a `.env` file or in your shell configuration.

In the `.env` file:
   ```bash
   DJANGO_SETTINGS_MODULE=dali.settings
   ```

To set this in your shell configuration, you can add the following line to your `.bashrc` or `.zshrc`:
   ```bash
   export DJANGO_SETTINGS_MODULE=dali.settings
   ```

### Docker Setup
This project uses Docker Compose to manage services such as the database, application, and web server.

- **Docker Compose**: Ensure Docker and Docker Compose are installed and properly configured on your machine.

- **Build the Docker Containers**:
   ```bash
   docker-compose build
   ```

- **Start the Docker Containers**:
   ```bash
   docker-compose up -d
   ```

- **Run Migrations in Docker**:
   ```bash
   docker-compose run --rm web poetry run python manage.py migrate
   ```

## Usage

### Run Django Development Server
To run the Django development server inside a Docker container, use the following command:
   ```bash
   docker-compose run --rm web poetry run python manage.py runserver
   ```

### CLI Commands
You can use the CLI for various operations. The available commands are:

- **List characters**:
   ```bash
   docker-compose run --rm -e DJANGO_SETTINGS_MODULE=dali.settings web poetry run python cli_typer.py list-characters
   ```

- **Delete a character**:
   ```bash
   docker-compose run --rm -e DJANGO_SETTINGS_MODULE=dali.settings web poetry run python cli_typer.py delete-character <character_id>
   ```

- **Show character stats**:
   ```bash
   docker-compose run --rm -e DJANGO_SETTINGS_MODULE=dali.settings web poetry run python cli_typer.py character-stats
   ```

- **Run the development server**:
   ```bash
   docker-compose run --rm web poetry run python cli_typer.py runserver
   ```

- **Show CLI Help**:
   ```bash
   docker-compose run --rm -e DJANGO_SETTINGS_MODULE=dali.settings web poetry run python cli_typer.py --help
   ```

## Testing

- To run tests locally, you can use the following command:
   ```bash
   poetry run pytest -vvv --no-header
   ```

- To run tests inside Docker:
   ```bash
   docker-compose run --rm -e DJANGO_SETTINGS_MODULE=dali.settings web poetry run pytest -vvv --no-header
   ```

## Makefile Commands

The Makefile contains useful commands for managing the application. Here are some of the common ones:

- **Start the Django server**:
   ```bash
   make start
   ```

- **Run migrations**:
   ```bash
   make migrate
   ```

- **Create migrations**:
   ```bash
   make migrations
   ```

- **Create a superuser**:
   ```bash
   make createsuperuser
   ```

- **Run tests**:
   ```bash
   make tests
   ```

- **Run Docker Compose tests**:
   ```bash
   make compose.tests
   ```

- **Start Docker Compose services**:
   ```bash
   make compose.start
   ```

- **Run Docker Compose migrations**:
   ```bash
   make compose.migrate
   ```

- **Create Docker Compose superuser**:
   ```bash
   make compose.superuser
   ```

- **Bootstrap Docker services**:
   ```bash
   make compose.bootstrap
   ```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Please ensure that your code adheres to the project's code style and includes relevant tests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
