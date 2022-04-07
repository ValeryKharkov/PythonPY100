if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 4, -3, -6, 8, 6, 9]

    list_average = sum(list_) / len(list_)


    new_list = [i - list_average for i in list_]  # Заполните список с помощью list comprehension

    print(new_list)
