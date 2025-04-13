

import os
import django

# Set the Django settings module path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KisanFriend.settings")

# Setup Django
django.setup()

globalinfo = {
    "user_name": None,
    "user_email": None
}