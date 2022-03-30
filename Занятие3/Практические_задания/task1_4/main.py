PI = 3.14


def square_circle(r):
    return PI * r ** 2


if __name__ == "__main__":
    square = square_circle(int(input('Enter r: ')))
    print(square)
