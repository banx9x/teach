def combination(n, k):
    if k > n:
        return 0

    if k == 0 or k == n:
        return 1

    # c(5, 3) -> n = 5, k = 3
    # c(4, 2) + c(4, 3)
    # c(3, 1) + c(3, 2) + c(3, 2) + c(3, 3)
    # -> 3 + c(3, 2) + c(3, 2) + 1
    # -> 4 + 2 * c(3, 2)
    # 4 + 2 * ( c(2, 1) + c(2, 2))
    # -> 4 + 2 * (2 + 1)
    # -> 4 + 2 * 3
    # -> 10
    return n if k == 1 else combination(n - 1, k - 1) + combination(n-1, k)


s = input("Enter two numbers (n, k): ")
s = s.split(sep=" ")

try:
    n = int(s[0])
    k = int(s[1])

    print(f"Combination({n}, {k}) = {combination(n, k)}")
except ValueError as e:
    print("Invalid numbers!!!")
