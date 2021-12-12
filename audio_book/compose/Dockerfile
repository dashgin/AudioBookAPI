FROM python:3.9-slim-bullseye

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy entrypoint.sh
COPY ./compse/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /usr/src/audio_book/entrypoint.sh
RUN chmod +x /entrypoint.sh

# copy project
COPY .. .

# run entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]