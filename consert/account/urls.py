from django.urls import path
from .views import *

app_name = 'account'
urlpatterns = [
    path("login/", Login, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", sign_up, name="sign_up"),
    path("profile/", profile, name="profile"),
    path("profile-edit/", profileEdit, name="profile-edit"),
    path("showfavorites/", showFavorites, name="show-favorites"),
]
