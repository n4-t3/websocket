# Django-WebSocket-Chat

![GitHub](https://img.shields.io/github/license/n4-t3/websockets?style=for-the-badge)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue?style=for-the-badge)
![Django Version](https://img.shields.io/badge/django-5.0.1%2B-green?style=for-the-badge)
![Poetry Version](https://img.shields.io/badge/poetry-1.7.1%2B-purple?style=for-the-badge)

Real-time chatting application built with Django and WebSocket, featuring 24-hour data retention and the creation of chat rooms using random codes.

## How to Locally Run the Project

Make sure you have Python 3.8 or higher installed. Install Poetry for managing the project's virtual environment.

```bash
# Install Poetry (if not already installed)
pip install poetry

# Install project dependencies
poetry install

# Activate the virtual environment
poetry shell

# Apply migrations
poetry run python manage.py migrate

# Run the development server
poetry run python manage.py runserver

```

## Contributions

Contributions are welcome! Feel free to create pull requests. 

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

