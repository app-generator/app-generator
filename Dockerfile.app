# syntax=docker/dockerfile:1
FROM nikolaik/python-nodejs:python3.12-nodejs22-slim

# build-time args to control non-root user uid/gid and name
ARG USERNAME=appuser
ARG USER_UID=1000
ARG USER_GID=1000

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    GIT_PYTHON_GIT_EXECUTABLE=/usr/bin/git \
    DJANGO_SETTINGS_MODULE=core.settings

WORKDIR /app

# Install system deps (as root). Use --no-install-recommends and clean apt cache.
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      git \
      libmariadb-dev \
      mariadb-client \
      gcc \
      make \
 && rm -rf /var/lib/apt/lists/*

# Copy and install Python deps
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Install npm global tool(s) (nodemon). This runs as root during build.
# If you prefer not to install globals, you can use npx or add devDependencies.
RUN npm install -g nodemon

# Copy project files
COPY . .

# Build frontend / assets as root (so it can write anywhere in /app)
# If your project uses yarn, run build now.
RUN yarn install --frozen-lockfile || yarn install \
 && yarn build \
 # docs build (if your image has make and sphinx; otherwise adjust)
 && if [ -d docs ]; then cd docs && rm -rf build && make html && sed -i 's/\/en\//\//g' build/html/sitemap.xml || true; fi

# Create a non-root user and make /app owned by that user.
# This uses build args UID/GID so you can match the host user (sm0ke).
RUN groupadd --gid ${USER_GID} ${USERNAME} || true \
 && useradd --uid ${USER_UID} --gid ${USER_GID} --create-home --shell /bin/bash ${USERNAME} || true \
 && chown -R ${USERNAME}:${USERNAME} /app

# Switch to non-root user for runtime
USER ${USERNAME}

# Ensure PATH and workdir are preserved
WORKDIR /app
EXPOSE 5005

# Note: No CMD provided — keep your original CMD/ENTRYPOINT in compose or add one here.
