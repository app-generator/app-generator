import os, shutil, requests, git
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.common.models import *
from helpers.docker_generator import *
from colorama import init, Fore
from colorama import Style

init(autoreset=True)

directory_path = 'cloned_repository'

tech_list = [
    "flask", "django", "nodejs", "nextjs", "react", "vue"
]

reference_dockerfile = """
FROM --platform=linux/amd64 nikolaik/python-nodejs:python3.9-nodejs20-slim
"""

def list_all_files_with_keyword(directory, keyword=None):
    all_files = []
    
    # Define a set of file extensions to exclude
    excluded_extensions = {
        '.svg', '.png', '.jpg', '.jpeg', '.gif', '.gitignore', 
        '.md', 'Dockerfile', 'docker-compose.yml', '.sh', '.sqlite3', 
        '.yml', '.css', '.html', '.ico'
    }
    
    # Using os.walk to traverse all subdirectories
    for root, dirs, files in os.walk(directory):
        # Exclude the .git directory from being traversed
        if '.git' in dirs:
            dirs.remove('.git')

        for file in files:
            # Exclude files with excluded extensions and files named `env.sample`
            if (keyword is None or keyword in file) and not any(file.endswith(ext) for ext in excluded_extensions):
                # Store full path for each valid file
                all_files.append(os.path.join(root, file))

    return all_files

def get_content(file_list):
    contents = ""
    for file_path in file_list:
        try:
            with open(file_path, 'r', encoding='utf-8') as infile:
                content = infile.read()
                contents += f"{content} \n\n"
        except Exception as e:
            print(Fore.RED + f"Error reading {file_path}: {e}\n\n")
    
    return contents

def groq_api_request(prompt):
    api_key = os.environ.get('GROQ_API_KEY')
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        'messages': [
            {'role': 'system', 'content': 'You are an assistant who specializes in authoring Dockerfiles for projects. Since you are an expert and know about their project, be definitive about recommendations.'},
            {'role': 'user', 'content': prompt}
        ],
        'model': 'llama3-8b-8192'
    }

    try:
        response = requests.post('https://api.groq.com/openai/v1/chat/completions', headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            print(Fore.RED + f"❌ Failed to get response from Groq API: {response.status_code}, {response.text}")
            return None
    except requests.exceptions.SSLError as ssl_error:
        print(Fore.RED + f"❌ SSL error occurred: {ssl_error}")
        return None

def clone_repository(repository_url):
    # Remove the directory if it already exists
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)

    # Clone the repository
    print(Fore.CYAN + "🔍 Cloning repository...")
    try:
        repo = git.Repo.clone_from(repository_url, directory_path)
        print(Fore.GREEN + "✅ Repository cloned successfully. \n")
    except Exception as e:
        print(Fore.RED + f"❌ Error cloning repository: {str(e)} \n")
        exit(1)

def generate_dockerfile_prompt(content):
    """Create the final merged content format."""

    final_content = f"""
        Generate a comprehensive Dockerfile for a monolithic web application that includes a Python backend and a JavaScript frontend in a single repository. This Dockerfile should support multiple frameworks and environments as follows:

        1. Backend:
        - Supported Frameworks: Python frameworks Django, Flask, or FastAPI.
        - Production Server: Use `gunicorn` (for Django, Flask) or `uvicorn` (for FastAPI) to serve backend applications in production, while development should use native commands like `manage.py runserver` for Django, `flask run` for Flask, and `uvicorn --reload` for FastAPI.
        - Environment Setup: Support dynamic configurations with environment variables for database URL, secret keys, allowed hosts, and other sensitive settings using `.env` files.
        - Static Files: Include steps for collecting and serving static files in production (e.g., `python manage.py collectstatic` for Django).

        2. Frontend:
        - Supported Frameworks: JavaScript frameworks Next.js, React, Vue, or Nuxt.js.
        - Build and Serve: In production, compile the frontend using `npm run build` and serve with `npm start` or an equivalent command. For development, use `npm run dev` to enable hot-reload functionality.

        3. Dockerfile Requirements:
        - Multi-stage Build: Use multi-stage builds to minimize the final image size, separating build and runtime stages.
        - Backend Dependencies: Install Python dependencies from `requirements.txt`.
        - Frontend Dependencies: Use Node.js to install JavaScript dependencies from `package.json`.
        - Environment Variables: Include ARG directives to manage environment variables for build and runtime settings.
        - Volume Setup: Enable volume mounting for live-reloading during development.

        4. Additional Configuration and Comments:
        - Provide inline comments within the Dockerfile to describe each step and configuration.
        - Include clear instructions on how to build and start the application in different environments.

        5. Only If multiple language:
        - using image for multiple plaform, example {reference_dockerfile}

        base on this information: {content}

        important result:
        - Dont return caption or describe, only script
        - Delete ```
        - Delete FINALIZE
        - Without Comment
        - if undefined version, using latest version
        """

    return final_content

def project_service_analyze(content):
    """Create a prompt for analyzing the project and returning a list of services with specifications."""
    
    # Start building the final content with basic analysis instructions
    final_content = (
        "- Analyze the project structure and dependencies to identify the different components that need to run as services.\n"
        "- Identify the relevant services.\n"
        "- For each component, provide a detailed list of services that should be included in the `docker-compose.yml` file.\n"
        "- Specify the following for each service:\n"
        "  - Service Name\n"
        "  - Image to use (include latest version)\n"
        "  - Build context if applicable\n"
        "  - Ports to map\n"
        "  - Volumes to mount\n"
        "  - Environment variables needed\n"
        "- Return the services in a structured format, such as a list, without any additional text or explanation.\n"
    )

    # Append project content
    final_content += f"- Project Content: {content}"

    return groq_api_request(final_content)

def generate_docker_compose_prompt(content):
    """Create the Docker Compose prompt based on the project content."""

    final_content = f"""
        Generate a comprehensive docker-compose.yml configuration for a monolithic web application that includes a Python backend and a JavaScript frontend in a single repository. This Docker Compose configuration should support the following:

        1. **Services**:
        - `backend`: Python backend service with Django, Flask, or FastAPI.
        - `frontend`: JavaScript frontend service using Next.js, React, Vue, or Nuxt.js.
        - `database`: PostgreSQL as the database, with volume persistence and environment configurations for database user, password, and name.
        - `third-party`: Include third-party tools with volume persistence and environment configurations for user, password, and name.

        2. **Volumes**: Configure volumes for backend and frontend codebases to enable live-reload functionality during development.

        3. **Network and Dependencies**: Configure internal networking between `backend` and `frontend` services, with `depends_on` for sequential startup, ensuring the database and third-party services are ready before the backend.

        4. **Port Mapping**: Expose necessary ports for external access, such as `8000` for the backend and `3000` for the frontend.

        5. **Restart Policy**: Set a restart policy to handle service crashes automatically.

        6. **Environment Variables**:
        - **Development and Production**: Use `.env` files for both environments, containing variables like `DATABASE_URL`, `SECRET_KEY`, `ALLOWED_HOSTS`, `FRONTEND_URL`, etc.
        - **Configuration Flexibility**: Allow overriding of default environment variables for greater flexibility in deployment and testing.

        7. **Additional Configuration and Comments**:
        - Provide inline comments within the docker-compose.yml file to describe each service and configuration.
        - Include clear instructions on how to build and start the containers for development and production, connect the frontend to the backend for API requests, and run migrations and seed data for the backend (if applicable).
        - Optimize commands for container restarts, rebuilds, and common troubleshooting tips.

        base on this information: {content}

        important result:
        - Dont return caption or describe, only script
        - Delete ```
        - Delete FINALIZE
        - Without Comment
        """

    return final_content

def extract_techs(input_string):
    
    return [tech for tech in tech_list if tech.lower() in input_string.lower()]

class Command(BaseCommand):
    help = 'Generate Docker Files for repos'

    def add_arguments(self, parser):
        parser.add_argument('-i', '--info', action='store_true', help='Print Help')
        parser.add_argument('-r', type=str, help='Repository URL')

    def handle(self, *args, **kwargs):
        ARG_HELP = kwargs['info']
        ARG_REPO = kwargs['r']

        if ARG_HELP:
            print(Fore.CYAN + Style.BRIGHT + " > HELP: Generator (CLI version)" + Style.RESET_ALL)
            print(Fore.YELLOW + "    -i (or --info)      : Print this help, and exit" + Style.RESET_ALL)
            print(Fore.YELLOW + "    -r <REPOSITORY>     : The Repository URL" + Style.RESET_ALL)
            print("")
            return

        if not ARG_REPO:
            print(Fore.RED + "❌ Error: Repository URL is required!" + Style.RESET_ALL)
            return

        print(Fore.GREEN + " > REPO: " + Style.BRIGHT + ARG_REPO + Style.RESET_ALL)
        clone_repository(ARG_REPO)

        print(Fore.BLUE + "🔍 Analyzing Project ..." + Style.RESET_ALL)

        env_files = list_all_files_with_keyword(directory_path, "env")
        files = list_all_files_with_keyword(directory_path)

        content_env = get_content(env_files)
        content = get_content(files)
        techs = extract_techs(content)
        services = project_service_analyze(content_env)

        print(Fore.BLUE + "\n🔍 Generating Dockerfile ..." + Style.RESET_ALL)
        dockerfile_prompt = generate_dockerfile_prompt(techs)

        result = groq_api_request(dockerfile_prompt).replace("```", "")

        with open('Dockerfile.generate', 'w') as dockerfile:
            dockerfile.write(result)

        print(Fore.BLUE + "🔍 Generating docker-compose.yml ... \n" + Style.RESET_ALL)
        docker_compose_prompt = generate_docker_compose_prompt(services)

        result_docker_compose = groq_api_request(docker_compose_prompt).replace("```", "")

        with open('docker-compose.generate.yml', 'w') as dockerfile:
            dockerfile.write(result_docker_compose)

        print(Fore.GREEN + "Successfully generated:")
        print(" ✅ Dockerfile.generate" + Style.RESET_ALL)
        print(" ✅ docker-compose.generate.yml\n" + Style.RESET_ALL)
