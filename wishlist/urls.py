from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_json
from wishlist.views import show_json_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
]