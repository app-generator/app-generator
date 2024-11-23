import os
import shutil
import subprocess
import requests
import git
import time
from django.core.management.base import BaseCommand
from colorama import init, Fore, Style
import yaml
import re

# Initialize colorama for styled CLI output
init(autoreset=True)

BASE_CLONE_DIR = 'cloned_repository'

DATABASE_KEYWORDS = ['database', 'db', 'postgres', 'mysql', 'sqlite']
FRAMEWORK_KEYWORDS = {
    'Flask': ['flask'],
    'Django': ['django'],
    'Next.js': ['next', 'next.config.js'],
    'React': ['react'],
    'Node.js': ['node', 'express'],
    'Vue': ['vue'],
}

DEFAULT_PORTS = {
    'Flask': '5000',
    'Django': '8000',
    'Next.js': '3000',
    'React': '3000',
    'Vue': '8080',
    'Node.js': '3000',
}

def clone_repository(repo_url, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    try:
        git.Repo.clone_from(repo_url, destination)
        print(Fore.GREEN + f"Repository cloned successfully to {destination}.")
    except Exception as e:
        print(Fore.RED + f"Error cloning repository: {e}")
        exit(1)

def list_all_files_with_keyword(directory, keyword=None):
    excluded_extensions = {
        '.svg', '.png', '.jpg', '.jpeg', '.gif', '.gitignore', '.md',
        'Dockerfile', 'docker-compose.yml', '.sh', '.sqlite3', '.yml',
        '.css', '.html', '.ico'
    }
    all_files = []
    for root, dirs, files in os.walk(directory):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if (keyword is None or keyword in file) and not any(file.endswith(ext) for ext in excluded_extensions):
                all_files.append(os.path.join(root, file))
    return all_files

def get_content(file_list):
    content = ""
    for file_path in file_list:
        try:
            with open(file_path, 'r', encoding='utf-8') as infile:
                content += infile.read() + "\n\n"
        except Exception as e:
            print(Fore.RED + f"Error reading {file_path}: {e}")
    return content

def detect_ports(content):
    ports = set()
    port_patterns = [
        r"port\s*=\s*(\d+)",
        r"PORT\s*=\s*(\d+)",
        r"\"port\":\s*(\d+)",
        r"\"PORT\":\s*(\d+)",
        r"-p\s*(\d+):",
    ]
    for pattern in port_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        ports.update(matches)
    return list(ports)

def detect_framework(content, all_files):
    if any('vue.config.js' in file or 'vite.config.js' in file for file in all_files):
        return "Vue"
    if "vue" in content.lower():
        return "Vue"
    if any('next.config.js' in file for file in all_files):
        return "Next.js"
    if "next" in content.lower():
        return "Next.js"
    if "react" in content.lower() and not any('next' in content.lower() for file in all_files):
        return "React"
    if any(keyword in content.lower() for keyword in FRAMEWORK_KEYWORDS['Node.js']):
        return "Node.js"
    return "Unknown"

def check_for_database(content):
    for keyword in DATABASE_KEYWORDS:
        if keyword in content.lower():
            return True
    return False

def prompt_user_confirmation(detected_info):
    print(Fore.CYAN + "Detected information:")
    for key, value in detected_info.items():
        print(Fore.YELLOW + f"  {key}: {value}")
    print(Fore.CYAN + "\nPress Enter to confirm, or modify the information below:")

    for key in detected_info.keys():
        while True:
            user_input = input(Fore.CYAN + f"{key} [{detected_info[key]}]: ").strip()
            if user_input:
                detected_info[key] = user_input
            confirmation = input(Fore.GREEN + f"Confirm {key} as {detected_info[key]}? (y/n): ").strip().lower()
            if confirmation == 'y':
                break

    return detected_info

def groq_api_request(prompt):
    api_key = os.getenv('GROQ_API_KEY')
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        'messages': [
            {'role': 'system', 'content': 'You are a Dockerfile and docker-compose.yml generation expert.'},
            {'role': 'user', 'content': prompt}
        ],
        'model': 'llama3-8b-8192'
    }
    try:
        response = requests.post('https://api.groq.com/openai/v1/chat/completions', headers=headers, json=data)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            content = content.replace("```", "").replace("FINALIZE", "").strip()
            return content
        else:
            print(Fore.RED + f"API Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Request Error: {e}")
        return None

def validate_yaml_content(yaml_content):
    try:
        yaml.safe_load(yaml_content)
        return True
    except yaml.YAMLError as exc:
        print(Fore.RED + f"YAML validation error: {exc}")
        return False

def save_invalid_content(directory, filename, content):
    invalid_path = os.path.join(directory, f"invalid_{filename}")
    with open(invalid_path, 'w') as f:
        f.write(content)
    print(Fore.RED + f"Invalid {filename} content saved to {invalid_path}")

class Command(BaseCommand):
    help = "Generate Dockerfile and docker-compose.yml for a repository"

    def add_arguments(self, parser):
        parser.add_argument('-r', '--repo', type=str, required=True, help='Repository URL')

    def handle(self, *args, **kwargs):
        repo_url = kwargs.get('repo')
        if not repo_url:
            print(Fore.RED + "Error: Repository URL is required.")
            return

        repo_name = os.path.basename(repo_url).replace(".git", "")
        timestamp = int(time.time())
        destination_dir = os.path.join(BASE_CLONE_DIR, f"{repo_name}-{timestamp}")

        if not os.path.exists(BASE_CLONE_DIR):
            os.makedirs(BASE_CLONE_DIR)

        print(Fore.GREEN + f"Cloning repository: {repo_url}")
        clone_repository(repo_url, destination_dir)

        print(Fore.BLUE + "Scanning project structure...")
        all_files = list_all_files_with_keyword(destination_dir)
        content_all = get_content(all_files)

        framework = detect_framework(content_all, all_files)
        print(Fore.YELLOW + f"Detected Framework: {framework}")
        ports = detect_ports(content_all) or [DEFAULT_PORTS.get(framework, "Unknown")]
        has_database = check_for_database(content_all)

        detected_info = {
            "Detected Framework": framework,
            "Detected Ports": ports,
            "Database Detected": has_database,
        }
        confirmed_info = prompt_user_confirmation(detected_info)

        # Generate Dockerfile
        dockerfile_prompt = f"""
        Generate a Dockerfile for a {confirmed_info['Detected Framework']} application:
        - Ports: {confirmed_info['Detected Ports']}
        - Database: {confirmed_info['Database Detected']}

        Important result:
        - Don't return any caption or describe, only script
        - Delete ```
        - Delete FINALIZE
        - Without Comment
        """
        print(Fore.BLUE + "Generating Dockerfile...")
        dockerfile_content = groq_api_request(dockerfile_prompt)
        dockerfile_path = os.path.join(destination_dir, 'Dockerfile')
        with open(dockerfile_path, 'w') as f:
            f.write(dockerfile_content)

        # Always generate docker-compose.yml
        docker_compose_prompt = f"""
        Generate a docker-compose.yml for a {confirmed_info['Detected Framework']} application:
        - Ports: {confirmed_info['Detected Ports']}
        """
        
        if str(confirmed_info['Database Detected']).lower() == "true":
            docker_compose_prompt += "- Include database service.\n"
        else:
            docker_compose_prompt += "- Do not include database service and depends_on.\n"

        docker_compose_prompt += """
        Important result:
        - Don't return any caption or describe, only script
        - Delete ```
        - Delete FINALIZE
        - Without Comment
        """

        print(Fore.BLUE + "Generating docker-compose.yml...")
        docker_compose_content = groq_api_request(docker_compose_prompt)

        if not validate_yaml_content(docker_compose_content):
            save_invalid_content(destination_dir, "docker-compose.yml", docker_compose_content)
        else:
            docker_compose_path = os.path.join(destination_dir, 'docker-compose.yml')
            with open(docker_compose_path, 'w') as f:
                f.write(docker_compose_content)

        print(Fore.GREEN + f"Generated files saved in {destination_dir}.")
