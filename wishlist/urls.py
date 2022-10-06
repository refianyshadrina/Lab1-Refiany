from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_json
from wishlist.views import show_json_by_id
from wishlist.views import register 
from wishlist.views import login_user
from wishlist.views import logout_user
from wishlist.views import show_ajax

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/submit/', show_ajax, name='add_wishlist'),
]