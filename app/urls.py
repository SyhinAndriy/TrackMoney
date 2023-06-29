from django.urls import path
from .views import *

urlpatterns = [
    path("", index_view, name='index'),
    path("app/cards/", cards_view, name='cards'),
    path("app/card-update/", update_card, name='card-update'),
    path("app/add_transaction/", add_transaction, name='add_transaction'),
    path("app/cards/new_card/", add_card, name='add_card'),
    path("app/cards/select_card/<int:card_id>", select_card, name='select_card'),
    path("app/statisctic", view_statistic, name='statistic'),
    path('api/data/', get_filtered_data, name='get_filtered_data'),


]
