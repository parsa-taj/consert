from django.urls import path
from .views import *

app_name = 'ticketSales'
urlpatterns = [
    path("conserts/", consertList, name="consert-list"),
    path("consert-detail/<int:pk>/", consertDetail, name="consert-detail"),
    path("", timeConsertList, name="timeConsert-list"),
    path("timeConsert-detail/<int:pk>/", timeConsertDetail, name="timeConsert-detail"),
    path("consert-edit/<int:pk>/", consertEditView, name="consert-edit"),
    path("location-edit/<int:pk>/", locationEditView, name="location-edit"),
    path("timeConsert-edit/<int:pk>/",
         timeConsertEditView, name="timeConsert-edit"),
    path("add-to-favorites/<int:pk>/", addToFavorites, name="add-to-favorites"),
    path("consertsInUserLocation/", consertsInUserLocation, name="consertsInUserLocation"),
]
