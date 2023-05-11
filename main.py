import math

def calculating(dist, weight, coef):
    if coef == 'СНГ':
        k = 0.35
    else:
        k = 0.3
    def set_weight(x):
        if '.' not in x and ',' not in x:
            return int(x)
        elif ',' in x:
            x = x.replace(',', '.')
            return float(x)
    weight = set_weight(weight)
    distance = int(dist)
    fuel_per_100 = 26 + (weight / 1000) * k
    result = (distance / 100) * fuel_per_100

    return math.ceil(result)







