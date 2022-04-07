if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }

    for fruit in cart:
        print(cart[fruit])  # получаем значение по ключу

    # посчитать через метод values
    print(sum(cart.values()))