"""
Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы AA часов в сутки, но пересыпать тоже
вредно и не стоит спать более BB часов. Сейчас Аня спит HH часов в сутки.
Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”.
Если Аня спит менее AA часов, выведите “Недосып”, если же более BB часов, то выведите “Пересып”.

Получаемое число AA всегда меньше либо равно BB.
"""
a = int(input()) #норма

b = int(input()) #пересып

v = int(input()) #аня

if v >= a and v <= b:

    print("Это нормально")

elif v > b:

    print("Пересып")

elif v < a:

    print("Недосып")