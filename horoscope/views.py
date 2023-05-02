from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}


def index(request):
    name_zodiac = list(zodiac_dict)
    li_zodiac = ""
    for sign in name_zodiac:
        redirect_path = reverse("horoscope-name", args=[sign])  # адрес строки для перехода по ссылке
        li_zodiac += f"<li> <a href='{redirect_path}'>{sign.title()}</a> </li>"
    li_zodiac += '<li style="font-size:30px; color:red"><a href="/horoscope/type">Type</a></li>'
    return HttpResponse(f"<ul>{li_zodiac}</ul>")


def type_zodiac(request):
    type_li = ["fire", "earth", "air", "water"]
    li_type = ""
    for value in type_li:
        redirect_path = reverse("type-name", args=[value])
        li_type += f"<li><a href='{redirect_path}'>{value.title()}</a></li>"
    return HttpResponse(f"<ul>{li_type}</ul>")


def types_zodiacs(request, sign_type):
    type_dict_zodiac = {"air": ["gemini", "libras", "aquarius"],
                        "fire": ["aries", "leo", "sagittarius"],
                        "water": ["pisces", "cancer", "scorpio"],
                        "earth": ["capricorn", "virgo", "taurus"]}
    li_zodiac_for_type = ""
    if sign_type in type_dict_zodiac:
        for sign in type_dict_zodiac.get(sign_type):
            redirect_path = reverse("horoscope-name", args=[sign])
            li_zodiac_for_type += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
        return HttpResponse(f"<ul>{li_zodiac_for_type}</ul>")



def get_info_zodiac(request, sign_zodiac: str):
    return HttpResponse(zodiac_dict.get(sign_zodiac, HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiac}")))


def get_info_zodiac_int(request, sign_zodiac: int):
    if 1 > sign_zodiac or sign_zodiac > 12:
        return HttpResponseNotFound(f"Неверный номер знака зодиака {sign_zodiac} ")
    name_zodiac = list(zodiac_dict)[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)
