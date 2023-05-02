from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("type/", views.type_zodiac),
    path("type/<sign_type>", views.types_zodiacs, name="type-name"),
    path("<int:sign_zodiac>/", views.get_info_zodiac_int),
    path("<str:sign_zodiac>/", views.get_info_zodiac, name="horoscope-name"),
]