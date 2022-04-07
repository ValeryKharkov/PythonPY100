def task(src_list: list) -> list:  # записать решение в виде функции
    return [i ** 3 if i > 0 else 0 for i in src_list]


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    new_list = task(list_)
    print(new_list)


# [i ** 2 if i % 2 == 0 else -i for i in range(10)]