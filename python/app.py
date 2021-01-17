# def hof(func):
#     def inner(p1, p2):
#         print("Mở rộng hàm")
#         print("Với mã bên ngoài")
#         print("Mà không làm thay đổi nội dung hàm")
#         func(p1, p2)  # gọi hàm, hàm được gọi trong hof

#     return inner


# def func(p1, p2):
#     print(p1)
#     print(p2)


# func = hof(func)  # func = inner

# func(135, "Dữ liệu")  # inner(135, "Dữ liệu")

# # tương tự với


# @hof
# def func(p1, p2):  # func ở đây là inner
#     print(p1)
#     print(p2)


# func(135, "Dữ liệu")

# # vậy nên nếu muốn truyền param vào thì truyền vào inner() hoặc hof() để func() sử dụng thôi


# class Complex:
#     # Hàm khởi tạo, nhận 2 tham số real và imag
#     def __init__(self, real, imag) -> None:
#         super().__init__()
#         self.real = float(real)  # gán cho 2 instance variable tương ứng
#         self.imag = float(imag)

#     def __str__(self) -> str:  # __str__ chuyển đổi object về dạng chuỗi
#         return f"({self.real}, i{self.imag})"

#     def __add__(self, other):  # __add__, __sub__, ... sử dụng khi thực hiện phép tính 2 object tương ứng
#         return f"({self.real + other.real}, i{self.imag + other.imag})"

#     def __sub__(self, other) -> str:
#         return f"({self.real - other.real}, i{self.imag - other.imag})"

#     def __abs__(self) -> float:
#         return self.real

#     def __eq__(self, other) -> bool:
#         return self.real == other.real and self.imag == other.imag


# # Nhập và cắt chuỗi ra
# s = input("Enter Complex(real, imag): ").split(",")
# # Eg: 1, 4 -> ["1", "4"]

# # c1 = Complex(1, 2)
# # c2 = Complex(3, 1)
# c1 = Complex(s[0], s[1])  # Complex("1", "4")

# def count_digit(n):
#     n //= 10
#     return 1 if n == 0 else 1 + count_digit(n)


# print(count_digit(130))


# def is_prime(n):
#     for i in range(2, n // 2):
#         if n % i == 0:
#             return False
#     else:
#         return True


# def print_pattern(n):
#     for i in range(1, n + 1):
#         s = str(i)
#         for j in range(i - 1, 0, -1):
#             s += f" {j}"

#         print(s)


# print_pattern(5)


# def factorial(n):
#     result = 1

#     for i in range(2, n + 1):
#         result *= i

#     return result


# def is_strong(n):
#     sum = 0

#     for i in str(n):
#         sum += factorial(int(i))

#     return sum == n


# print(f"145 {is_strong(145)}")


# def count_digit(n):
#     if n == 0:
#         return 0
#     else:
#         return 1 + count_digit(n // 10)


# print(count_digit(2423242309090))
# n == 0 -> False
# 3

# def binary_search(list, n):
#     print(list)
#     if len(list) == 1:
#         return list[0] == n

#     mid = len(list) // 2

#     if list[mid] == n:
#         return True
#     elif list[mid] > n:
#         return binary_search(list[:mid], n)
#     else:
#         return binary_search(list[mid + 1:], n)


# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 1))

# def cal(n):
#     if n == 0:
#         raise ValueError("n can not be zero")
#     return 10 / n


# try:
#     print(cal(1))
# except ValueError as e:
#     print(e)  # n can’t not be zero

def find_max(list): 
    if len(list) == 1:
        return list[0]
    else:
        the_rest = find_max(list[1:])
        return list[0] if list[0] > the_rest else the_rest


print(find_max([1, 4, 2, 3, 6, 4, 6, 9]))
