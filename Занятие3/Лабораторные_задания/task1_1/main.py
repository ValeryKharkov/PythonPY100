def main():
    n = 1  # первое натуральное число
    current_sum = 0  # текущая сумма
    max_sum = 500  # максимальная сумма
    # count_numbers = 0
    # TODO  найти количество чисел сумма квадратов, которых не превышает 500
    while True:

        if current_sum >= max_sum:
            break
        current_sum += n ** 2
        n += 1
    return n - 1, current_sum - n ** 2


if __name__ == "__main__":
    count_numbers, sum_ = main()
    print(count_numbers, sum_)
