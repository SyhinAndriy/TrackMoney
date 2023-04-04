from django.urls import path
from .views import *

urlpatterns = [
    path("app/", index_view, name='index'),
]
