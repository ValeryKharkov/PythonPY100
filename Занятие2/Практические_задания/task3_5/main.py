mount = int(input('Введи номер месяца: '))

if mount in [3, 4, 5]:
    print("Весна")
elif mount in [6, 7, 8]:
    print("Лето")
elif mount in (9, 10, 11):
    print("Осень")
elif mount in {12, 1, 2}:
    print("Зима")
else:
    print('Введи число от 1 до 12')# TODO добавить блок else и выдавать пользователю любое предупреждение о том, что месяц указан неверно
