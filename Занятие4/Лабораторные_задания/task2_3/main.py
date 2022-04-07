def task(num: int) -> bool:  # добавить аннотацию типов
    num = abs(num)
    list_ = [int(i) for i in str(num)] # TODO найти сумму цифр числа и понять двузначная ли она
    if len(list_) == 2:
        return True
    else:
        return False

if __name__ == "__main__":
    print(task(12))
    print(task(555))
    print(task(-12))
    print(task(-149))