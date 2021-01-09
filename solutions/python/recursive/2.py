def fact(n):
    if n <= 0:
        return -1

    # fact(5) n = 5
    # 5 * fact(4)
    # 5 * 4 * fact(3)
    # 5 * 4 * 3 * fact(2)
    # 5 * 4 * 3 * 2 * fact(1)
    # 5 * 4 * 3 * 2 * 1
    # -> 120
    return 1 if n == 1 else n * fact(n - 1)


try:
    n = int(input("Enter an integer: "))

    print(f"Factorial({n}) = {n}! = {fact(n)}")
except ValueError:
    print("Invalid number!!!")
