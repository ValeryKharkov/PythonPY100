def count_even_numbers(list_numbers: list) -> int:
    return len([i for i in list_numbers if i % 2 == 0])  # найти количество четных чисел в списке list_numbers


if __name__ == "__main__":
    print(count_even_numbers(list(range(1, 25))))
