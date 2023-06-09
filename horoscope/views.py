from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {
    'aries': (
        'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).', {3: range(21, 32), 4: range(1, 21)}),
    'taurus': (
        'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).', {4: range(21, 31), 5: range(1, 22)}),
    'gemini': (
        'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).', {5: range(22, 32), 6: range(1, 22)}),
    'cancer': ('Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).', {6: range(22, 31), 7: range(1, 23)}),
    'leo': ('Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).', {7: range(23, 32), 8: range(1, 22)}),
    'virgo': (
        'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
        {8: range(22, 32), 9: range(1, 24)}),
    'libra': (
        'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
        {9: range(24, 31), 10: range(1, 24)}),
    'scorpio': ('Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
                {10: range(24, 32), 11: range(1, 23)}),
    'sagittarius': ('Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
                    {11: range(23, 31), 12: range(1, 23)}),
    'capricorn': ('Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
                  {12: range(23, 32), 1: range(1, 21)}),
    'aquarius': ('Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
                 {1: range(21, 31), 2: range(1, 20)}),
    'pisces': (
        'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
        {2: range(20, 29), 3: range(1, 21)}),
}


#
# def get_years(request, sign_zodiac):
#     return HttpResponse(f"Вы передали строку - {sign_zodiac}")


def index(request):
    name_zodiac = list(zodiac_dict)
    contex_dict = {"zodiacs": name_zodiac
                   }
    return render(request, "horoscope/index.html", context=contex_dict)


def type_zodiac_menu(request):
    type_li = [("fire", "огонь"), ("earth", "земля"), ("air", "воздух"), ("water", "вода")]
    type_zodiac_dict = {"type_li": type_li}
    return render(request, 'horoscope/type_zodiac_menu.html', context=type_zodiac_dict)


def types_zodiacs(request, sign_type):
    type_dict_zodiac = {"air": ["gemini", "libra", "aquarius"],
                        "fire": ["aries", "leo", "sagittarius"],
                        "water": ["pisces", "cancer", "scorpio"],
                        "earth": ["capricorn", "virgo", "taurus"]}
    data_dict = {"type_dict_zodiac": type_dict_zodiac,
                 "sign_type": sign_type}
    return render(request, 'horoscope/types_zodiacs.html', context=data_dict)


def get_info_zodiac(request, sign_zodiac: str):
    if sign_zodiac in zodiac_dict:
        name_zodiac = list(zodiac_dict)
        description = zodiac_dict.get(sign_zodiac)[0]
        data = {"description_in_dict": description,
                "sign_in_dict": description.split()[0],
                "name_zodiac": name_zodiac
                }
        return render(request, 'horoscope/info_zodiac.html', context=data)
    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiac}")


def get_zodiac_date(request, month, day):
    for key, value in zodiac_dict.items():
        redirect_path = reverse("horoscope-name", args=[key])
        if month in value[1] and day in value[1].get(month):
            return HttpResponseRedirect(redirect_path)
    return HttpResponseNotFound('Знак зодиака не найден')


def get_info_zodiac_int(request, sign_zodiac: int):
    if 1 > sign_zodiac or sign_zodiac > 12:
        return HttpResponseNotFound(f"Неверный номер знака зодиака {sign_zodiac} ")
    name_zodiac = list(zodiac_dict)[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)
