from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("", views.index, name="horoscope-index"),
    path("type/", views.type_zodiac, name="zodiac-types"),
    path("type/<str:sign_type>", views.types_zodiacs, name="type-name"),
    # path("<yyyy:sign_zodiac>/", views.get_years),
    path("<int:sign_zodiac>/", views.get_info_zodiac_int),
    path("<str:sign_zodiac>/", views.get_info_zodiac, name="horoscope-name"),
    path("<int:month>/<int:day>", views.get_zodiac_date)
]