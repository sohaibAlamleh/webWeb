# awesome_website/urls.py

from django.urls import include,re_path as url
from django.contrib import admin



urlpatterns = [
    url("", include("account.urls")),
    url(r"admin/", admin.site.urls),


]