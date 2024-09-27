# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
License: MIT
"""

import os, sys, json
from pprint import pp

from helpers.util import *

class ApplicationDetector:
    def __init__(self, repo_path):

        # first two levels 
        self.files = []
        self.repo_type = COMMON.NA 
        self.repo_path = Path(repo_path)

    def detect(self):
        if self._has_file('requirements.txt'):
            if self._has_file('manage.py'):
                self.repo_type = COMMON.TYPE_DJANGO
                return self.repo_type
            else:
                self.repo_type = COMMON.TYPE_FLASK
                return self.repo_type
        else:
            return COMMON.NA

    def _has_file(self, filename):
        return (self.repo_path / filename).exists()

class Dockerizer:
    def __init__(self, repo_path, app_type):
        self.repo_path = Path(repo_path)
        self.app_type = app_type
        self.strategies = {
            COMMON.TYPE_DJANGO  : DjangoDockerStrategy (),
            COMMON.TYPE_FLASK   : FlaskDockerStrategy  (),
        }

    def generate_files(self):
        strategy = self.strategies.get(self.app_type)
        if strategy:
            strategy.generate_dockerfile(self.repo_path)
            strategy.generate_docker_compose(self.repo_path)
            return COMMON.OK
        else:
            #raise ValueError(f"No strategy for {self.app_type}")
            print( ' > ERR: Unknown repo type' )
            return COMMON.NA

class DockerStrategy:

    status         = COMMON.NA     
    dockerfile     = None 
    docker_compose = None

    def generate_dockerfile(self, repo_path):
        raise NotImplementedError

    def generate_docker_compose(self, repo_path):
        raise NotImplementedError

class DjangoDockerStrategy(DockerStrategy):
    def generate_dockerfile(self, repo_path):
        dockerfile_content = """ DOCKER file CONTENT -> Django """
        self.dockerfile = dockerfile_content

    def generate_docker_compose(self, repo_path):
        docker_compose_content = """ DOCKER_COMPOSE file CONTENT -> Django """
        self.docker_compose = docker_compose_content

    def get(self):
        return self.status, self.dockerfile, self.docker_compose            

class FlaskDockerStrategy(DockerStrategy):
    def generate_dockerfile(self, repo_path):
        dockerfile_content = """ DOCKER file CONTENT -> Flask """
        self.dockerfile = dockerfile_content

    def generate_docker_compose(self, repo_path):
        docker_compose_content = """ DOCKER_COMPOSE file CONTENT -> Flask """
        self.docker_compose = docker_compose_content

    def get(self):
        return self.status, self.dockerfile, self.docker_compose
