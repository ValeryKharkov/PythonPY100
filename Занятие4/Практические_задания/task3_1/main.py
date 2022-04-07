def dict_over_for_loop(n: int) -> dict:
    dict_ = {}
    for i in range(n):
        dict_[i] = i ** 2  # присвоение словарю нового значения по несуществующему ранее ключу

    return dict_


def dict_comprehension(n: int) -> dict:
    return {i: i ** 2 for i in range(n)}  # записать dict comprehension


if __name__ == "__main__":
    number = 10
    print(dict_over_for_loop(number))
    print(dict_comprehension(number))
