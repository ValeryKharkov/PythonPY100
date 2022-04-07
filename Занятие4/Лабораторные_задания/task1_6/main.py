if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    list_great_first = [i for i in list_ if i > list_[0]]  # отфильтровать элементы больше первого
    print(len(list_great_first))