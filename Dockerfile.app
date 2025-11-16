FROM nikolaik/python-nodejs:python3.12-nodejs22-slim

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    GIT_PYTHON_GIT_EXECUTABLE=/usr/bin/git \
    DJANGO_SETTINGS_MODULE=core.settings

# Install system deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        libmariadb-dev \
        mariadb-client \
        gcc \
        make && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Install global npm tools
RUN npm install -g nodemon

# Copy everything
COPY . .

# Build frontend + docs (if exists)
RUN yarn install --frozen-lockfile || yarn install && \
    yarn build && \
    if [ -d docs ]; then \
        cd docs && \
        rm -rf build && \
        make html && \
        sed -i 's/\/en\//\//g' build/html/sitemap.xml || true; \
    fi

# Create non-root user (auto UID/GID, no conflict)
RUN useradd -m -s /bin/bash appuser && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

EXPOSE 5005

WORKDIR /app
