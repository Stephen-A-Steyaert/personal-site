from django.contrib import admin
from django.urls import path, include # type: ignore
from django.urls.resolvers import URLPattern, URLResolver
from typing import Union

urlpatterns: list[Union[URLPattern, URLResolver]] = [
    path("admin/", admin.site.urls),
]
