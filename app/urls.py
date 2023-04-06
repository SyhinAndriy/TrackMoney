from django.urls import path
from .views import *

urlpatterns = [
    path("app/", index_view, name='index'),
    path("app/cards", cards_view, name='cards'),
    path("app/card-update/", update_card, name='card-update'),

]
