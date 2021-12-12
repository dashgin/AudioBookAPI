from .base import * # noqa
import os
from .base import BASE_DIR
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=0))


# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with ',' between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default="127.0.0.1,0.0.0.0,localhost").split(",")

STATIC_ROOT = BASE_DIR / "staticfiles"
