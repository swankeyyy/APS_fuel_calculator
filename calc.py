import math

def set_country():
    """"Ввод страны"""
    country = input('Введите страну: ')
    return country

def country_coefficient(country):
    coefficients = {0.45: 'TR-GE-AZ',
                    0.35: 'RUS-KZ-UZ-KG-CHN-MN',
                    0.3: 'BY'}

    long_names_countries = {
        'TR': 'tr, turk, turcija, турция, турки, turkey, tr',
        'GE': 'ge, грузия, georgiz, ge, гр',
        'AZ': 'az, азеры, азерботы, азербайджа, azerbaijan',
        'KZ': 'kz, казашка, казахстан, kazahstan',
        'UZ': 'uz, узбечка, узбекистан, uzbekistan',
        'KG': 'kg, киргизия, кыргызтан, киргизтан, kirgistan',
        'CHN': 'chn, китай, чайна, ch',
        'MN': 'mn, монголия, монгол, mongol, mongolya',
        'BY': 'by, belarus, беларусь, белоруссия, домой, дом',
        'RUS': 'rus, россия, russia, раша, рус'
    }

    coefficients_item = 'aaa'

    for item in long_names_countries:
        if country.lower() in long_names_countries[item]:
            coefficients_item = item

    for coefficient in coefficients.keys():
        if coefficients_item in coefficients[coefficient]:
            return coefficient

    return set_country()

def set_weight():
    """"Ввод расстояния, если не целое то ',' меяет на '.'"""

    weight = input('Введите вес в килограммах с точностью до грамм: ')
    if '.' not in weight and ',' not in weight:
        return int(weight)
    elif ',' in weight:
        weight = weight.replace(',', '.')

    return float(weight)

def calculating():
    coef = country_coefficient(set_country())
    weight = set_weight()
    distance = int(input('Введите расстояние (целое число): '))
    fuel_per_100 = 26 + (weight / 1000) * coef
    print(f'Ваш расход на 100 км составляет {fuel_per_100} литров')

    result = (distance / 100) * fuel_per_100

    return math.ceil(result)

print(calculating())







