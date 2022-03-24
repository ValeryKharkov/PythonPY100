def pow_func(base, pow_=2):
    print(base, "**", pow_)
    return base ** pow_


if __name__ == "__main__":
    print(pow_func(4))  # по умолчанию возводим число в степень два
    print(pow_func(3, pow_=3))  # переопределяем аргумент по умолчанию

    print(pow_func(2, 5))  # используем позиционные аргументы
    print(pow_func(pow_=2, base=8))  # используем позиционные аргументы
