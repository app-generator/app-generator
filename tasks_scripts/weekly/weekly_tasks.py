import sys
import os
import django

current_file_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_file_dir, '../..'))
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User


def main(argv):
    users = []
    for user in User.objects.all():
        users.append(user.username)
    print(users)

if __name__ == '__main__':
    main(sys.argv)
