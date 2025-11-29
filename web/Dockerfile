FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.9.13 /uv /bin/uv

WORKDIR /app/web
COPY . /app/web

# psycopg2 ビルドに必要なパッケージをインストール
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     libpq-dev \
#     postgresql-client \
#     && uv sync --frozen --no-dev \
#     && apt-get purge -y build-essential libpq-dev \
#     && apt-get autoremove -y \
#     && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libpq-dev \
        gcc \
        python3-dev \
    && uv sync --frozen --no-dev
    && rm -rf /var/lib/apt/lists/*
