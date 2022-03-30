def input_numbers():
    ...  # TODO выберите нужный цикл, чтобы получать числа с клавиатуры
    # input_number = int(input('Enter number: '))
    list_number = []

    # while input_number >= 0:
    #     if 3 <= input_number <= 13:
    #         list_number.append(input_number)
    #
    #     input_number = int(input('Enter number: '))
    #
    # return list_number

    while True:
        input_number = int(input('Enter number: '))
        if input_number < 0:
            break

        if 3 <= input_number <= 13:
            list_number.append(input_number)

        # input_number = int(input('Enter number: '))

    return list_number

if __name__ == "__main__":
    numbers = input_numbers()
    print(numbers)
