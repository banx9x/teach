# Viết hàm sum(n) nhận vào một số nguyên dương n, tính và trả về tổng các số từ 1 -> n, sử dụng đệ quy

def sum(n):
    return 1 if n == 1 else n + sum(n - 1)


# Viết hàm factorial(n) nhận vào một số nguyên dương n, tính và trả về kết quả phép tính n! (giai thừa của n), sử dụng đệ quy

def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)

# Viết hàm factorial(n) nhận vào một số nguyên dương n, tính và trả về kết quả phép tính n! (giai thừa của n), sử dụng đệ quy


def fibonacci(n):
    return 1 if n == 1 or n == 2 else fibonacci(n - 1) + fibonacci(n - 2)


# Viết hàm count_digit(n) trả về số chữ số của số nguyên n, sử dụng đệ quy

def count_digit(n):
    n //= 10
    return 1 if n == 0 else 1 + count_digit(n)


# Viết hàm find_gcd(a, b) nhận vào 2 số nguyên a, b. Trả về ước chung lớn nhất của 2 số

def find_gcd(a, b):
    return a if a == b else find_gcd(a - b, b) if a > b else find_gcd(a, b - a)

# Viết hàm binary_search(list, n) nhận vào một list số nguyên đã được sắp xếp, và một giá trị n. Kiểm tra giá trị n có trong list hay không, kết quả trả về True hoặc False, triển khai giải thuật tìm kiếm nhị phân, sử dụng đệ quy


def binary_search(l, n):
    if len(l) == 1:
        return l[0] == n

    mid = len(l) // 2

    if l[mid] == n:
        return True
    else:
        return binary_search(l[0:mid], n) if n < l[mid] else binary_search(l[mid:], n)


def count_str(s):
    d = dict({})

    for c in s:
        if c == " ":
            continue
        
        if d.get(c):
            d[c] += 1
        else:
            d[c] = 1

    l = list(d.items())
    l.sort(key=lambda i: i[1])
    return l[-1]


print(count_str("Xin chào các bạn, mình là Ba"))
