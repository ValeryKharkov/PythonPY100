# TODO запишите здесь функцию factorial
def factorial(n):
    factorial_ = 1
    for i in range(1, n + 1):
        # print(i)
        factorial_ *= i
    return factorial_

if __name__ == "__main__":
    # TODO распечатать результат выполнения функции factorial от числа 5
    print(factorial(int(input('Enter n: '))))