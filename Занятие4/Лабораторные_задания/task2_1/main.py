if __name__ == "__main__":
    number = 123456789

    list_digits = [int(i) for i in list(str(number))]  # c помощью list comprehension получить список цифр числа
    print(list_digits)

    print(sum(list_digits))  # найти сумму цифр числа

    print(sum([i for i in list_digits if i % 2 == 0]))  # найти сумму всех четных чисел

    print(len(list_digits))  # найти количество цифр

    print(min(list_digits))  # найти минимальную цифру

    print(list_digits[::2])  # все цифры стоящие на нечетных местах

    print(list_digits[0] - list_digits[-1])  # найти разность между первой и последней цифрой
