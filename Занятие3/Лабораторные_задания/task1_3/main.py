def get_list_number_divisors(number):
      # TODO найти список делителей числа number
    result = []

    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return result


if __name__ == "__main__":
    print(get_list_number_divisors(2 ** 16))
