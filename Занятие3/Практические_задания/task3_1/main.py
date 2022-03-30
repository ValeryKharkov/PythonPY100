def remove_whitespace(str_):
    words_list = str_.split(' ')  # TODO разделить строку по пробелам
    print(words_list)

    words_list_without_empty_string = []
    for word in words_list:
        if word:
            words_list_without_empty_string.append(word)# TODO поместить в результирующий список все слова
    print(words_list_without_empty_string)

    return ' '.join(words_list_without_empty_string)  # TODO соединить список слов в строку


if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    print(remove_whitespace(str_with_space))
