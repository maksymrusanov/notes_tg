FROM ghcr.io/astral-sh/uv:alpine 
RUN apk add --no-cache uv 
COPY . /app
WORKDIR /app
RUN uv sync --no-dev
CMD ["uv", "run", "python3", "main.py"]
