from django.urls import include, re_path as  url
from account.views import dashboard, register

urlpatterns = [
    url(r"accounts/", include("django.contrib.auth.urls")),
    url(r"dashboard/",dashboard, name="dashboard"),
    url(r"oauth/", include("social_django.urls")),
    url(r"register/", register, name="register"),
]