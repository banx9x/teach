def cal(n):
    if n == 0:
        raise ValueError("n can't not be zero")

    return 10 / n


try:
    cal(0)
except ValueError as e:
    print(e)
