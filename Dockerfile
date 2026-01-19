FROM python:3.12-slim AS builder
WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock* ./
RUN uv pip install --system .

FROM python:3.12-slim
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages \
    /usr/local/lib/python3.12/site-packages

# Copy app code
COPY . .

EXPOSE 7860
CMD [ "python", "app.py" ]