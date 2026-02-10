import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "intelligent_hospital_managementsystem.settings")
django.setup()

from myapp.models import login_table

username = 'admin'
password = 'admin'
user_type = 'admin'

if login_table.objects.filter(username=username).exists():
    print(f"User '{username}' already exists. Updating...")
    user = login_table.objects.get(username=username)
    user.password = password
    user.type = user_type
    user.save()
else:
    print(f"Creating user '{username}'...")
    user = login_table(username=username, password=password, type=user_type)
    user.save()

print("User created/updated successfully.")
