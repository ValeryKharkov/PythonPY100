def check_string(str_):

    if not str_:
        return False

    str_ = set(str_)
    base = set('01')
    for i in str_:
        if i not in base:
            return False
        else:
            return True



if __name__ == "__main__":
    print(check_string("1010101010"))
    print(check_string("101021231010103"))
    print(check_string("asdawqe"))
    print(check_string(""))
