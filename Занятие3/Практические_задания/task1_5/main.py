def counter():
    count_local = count + 1

    return count_local


if __name__ == "__main__":
    count = 0
    print(counter())  # что будет выведено?
