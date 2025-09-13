FROM nikolaik/python-nodejs:python3.12-nodejs22-slim

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GIT_PYTHON_GIT_EXECUTABLE=/usr/bin/git
ENV DJANGO_SETTINGS_MODULE=core.settings

COPY requirements.txt .

RUN apt update && apt install -y git libmariadb-dev mariadb-client gcc make

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install dependencies
RUN npm install -g nodemon

COPY . .

# RUN yarn ; yarn build 
RUN pnpm i ; pnpm run build
RUN cd docs && rm -rf build && make html && sed -i 's/\/en\//\//g' build/html/sitemap.xml

EXPOSE 5005
