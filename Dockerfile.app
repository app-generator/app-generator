FROM nikolaik/python-nodejs:python3.9-nodejs20-slim

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GIT_PYTHON_GIT_EXECUTABLE=/usr/bin/git
ENV DJANGO_SETTINGS_MODULE=core.settings

COPY requirements.txt .

RUN apt update
RUN apt install -y git libmariadb-dev mariadb-client gcc

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install dependencies
RUN apt-get update && apt-get install -y make
RUN npm install -g nodemon

COPY . .

RUN yarn ; yarn build
RUN cd docs && rm -rf build && make html && sed -i 's/\/en\//\//g' build/html/sitemap.xml

EXPOSE 5005
