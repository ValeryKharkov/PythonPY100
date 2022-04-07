def list_over_for_loop(n):
    list_ = []
    for i in range(n):
        list_.append(i ** 2)

    return list_


def list_comprehension(n):
    return [i ** 2 for i in range(n)]  # записать list comprehension


if __name__ == "__main__":
    num = 10
    print(list_over_for_loop(num))
    print(list_comprehension(num))
