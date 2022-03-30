if __name__ == "__main__":
    # Write your solution here
    pass
list_ = [1, 4, -6, 0, 7, 13, 7, -4, 9, 10]

max_index = list_.index(max(list_))
print(max_index)
list_[0], list_[max_index] = list_[max_index], list_[0]
print(list_)
