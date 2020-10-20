from django.urls import re_path

from demi.index.views import IndexHandler

urlpatterns = [
    re_path("^index/$", IndexHandler.as_view())
]