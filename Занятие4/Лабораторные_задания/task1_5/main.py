if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    list_even = [i for i in list_ if i % 2 == 0]  # получить два списка четных и нечетных чисел
    list_odd = [i for i in list_ if i % 2 != 0]

    len_list_even = len(list_even) # найти длины этих списков
    len_list_odd = len(list_odd)

    if len_list_even > len_list_odd:
        print('четных больше')
    elif len_list_even < len_list_odd:
        print('нечетных больше')
    else:
        print('четных и нечетных одинаково')
    # распечатать каких чисел больше. Учтите, что длины могу быть равны
