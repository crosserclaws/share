FROM python:3.11-slim-bullseye

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY src/ /src/
COPY pyproject.toml /pyproject.toml
RUN pip install -e /
COPY tests/ /tests/

WORKDIR /src
ENV FLASK_APP=allocation/entrypoints/flask_app.py FLASK_DEBUG=1 PYTHONUNBUFFERED=1
CMD flask run --host=0.0.0.0 --port=80
