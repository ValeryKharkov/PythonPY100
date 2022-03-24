list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3]

count_even = 0  # количество четных чисел
count_odd = 0  # количество нечетных чисел

# TODO посчитать количество четных и нечетных значений в списке
for i in list_:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
if count_even > count_odd:
    print('Четных чисел больше')
else:
    print('Нечетных чисел больше')
