def task(num: int):
    list_ = [int(digit) for digit in str(num)]  # сформировать список цифр

    if (4 in list_ and 8 in list_) or 9 in list_:  # записать условие
        print("Входят цифры (4 и 8) или цифра 9")
    else:
        print("Не входят цифры (4 и 8) или цифра 9")


if __name__ == "__main__":
    task(1234)
    task(12345678)
    task(1235679)
    task(0)
