wind = int(input())

if 1 <= wind <= 4:
    print("слабый (1)")
elif 5 <= wind <= 10:
    print("умеренный (2)")
elif 11 <= wind <= 18:
    print("сильный (3)")
elif wind > 19:
    print("ураганный (4)")
else:
    print("Такого ветра не бывает")
