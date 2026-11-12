import hashlib

from django.conf import settings
from django.urls import path

from . import views

AB_PATH = hashlib.sha1(settings.TEAM_NICKNAME.encode()).hexdigest()[:7]

urlpatterns = [
    path(f"{AB_PATH}", views.page, name="abtest-page"),
    path(f"{AB_PATH}/click", views.click, name="abtest-click"),
    path(f"{AB_PATH}/stats", views.stats, name="abtest-stats"),
]
