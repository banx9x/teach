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

# def find_max(list):
#     if len(list) == 1:
#         return list[0]
#     else:
#         the_rest = find_max(list[1:])
#         return list[0] if list[0] > the_rest else the_rest


# print(find_max([1, 4, 2, 3, 6, 4, 6, 9]))


# def sum(l):
#     s = 0

#     for i in l:
#         s += i if type(i) == int else sum(i) if type(i) == list else 0

#     return s


# print(sum([1, 2, [3, 4, [5, 6, "text", True]]]))


# def getData(f_one, f_two):
#     def container(func):
#         def inner(param, data):
#             func(param, data)
#             new_list = []
#             mapped_data = f_one(data)
#             f_two(param, mapped_data, new_list)

#             return new_list
#         return inner
#     return container


# def f_one(data):
#     for i in range(len(data)):
#         data[i] *= 2

#     return data


# def f_two(param, data, new_list):
#     for i in data:
#         if i > param:
#             new_list.append(i)


# demo_list = [1, 2, 56, 78, 3]


# @getData(f_one, f_two)
# def check(param, data):
#     print("Do nothing here 😉")


# number = int(input("Enter a number: "))

# data = check(number, demo_list)
# print(data)  # [112, 156]

# def deco(f):
#     def inner(*args, **kwargs):
#         print("deco")
#         f(*args, **kwargs)
#     return inner


# def hof(f):
#     def inner(*args, **kwargs):
#         print("hof")
#         f(*args, **kwargs)
#     return inner


# @deco
# @hof
# def lol(x):
#     print(x)


# lol(10)

# age = 15
# message = "Lớn hơn 30" if age >= 30 else "Lớn hơn 20" if age >= 20 else "Lớn hơn 10" if age >= 10 else "Nhỏ hơn 10"
# print(message)
# print(type(range(10)))

# for name in ["Ba", "Béo", "Ú"]:
#     if name == "Ú":
#         print("Found")
#         break
# else:
#     print("Not found")


# def sum(a, b, *numbers, **kwargs):
#     print(kwargs)
#     total = a + b

#     for n in numbers:
#         total += n if type(n) == int or type(n) == float else 0

#     for key in kwargs:
#         total += kwargs[key]

#     return total


# print(sum(1, 2, 3, 4, 5, 6, 7, 1.4, "ABC", True, c=100, d=120))


# 1. Viết chương trình yêu cầu nhập một số nguyên n, kiểm tra và in ra số đó có chia hết cho cả 3 và 5 hay không

# Ví dụ:

# Nhập một số nguyên: 5
# 5 không chia hết cho cả 3 và 5

def check_div(n):
    return n % 3 == 0 and n % 5 == 0


# print(check_div(int(input("Nhập n: "))))

# 2. Viết chương trình yêu cầu nhập 3 số a, b, c. Kiểm tra và in ra số lớn nhất

# Ví dụ:

# Nhập số a: 1
# Nhập số b: 2
# Nhập số c: 3
# Số lớn nhất trong 3 số[1 2 3] là 3
# def max_of_three(a, b, c):
#     return a if a >= b and a >= c else b if b >= a and b >= c else c


# a = int(input("Nhap a: "))
# b = int(input("Nhap b: "))
# c = int(input("Nhap c: "))
# print(max(a, b, c))
# 3. Viết chương trình yêu cầu nhập 3 số a, b, c tương ứng với độ dài 3 cạnh tam giác. Kiểm tra và in ra 3 số có tạo thành một tam giác hợp lệ hay không

# Ví dụ:

# Nhập cạnh a: 1
# Nhập cạnh b: 3
# Nhập cạnh c: 3
# [1 3 3] là một tam giác hợp lệ

# def is_triangle(a, b, c):
#     return a + b > c and a + c > b and b + c > a


# a = int(input("Nhap a: "))
# b = int(input("Nhap b: "))
# c = int(input("Nhap c: "))

# print(is_triangle(a, b, c))

# 4. Viết chương trình yêu cầu nhập 3 số a, b, c. Kiểm tra và in ra 3 số là dãy tăng dần(a < b < c), giảm dần(a > b > c) hay không

# Ví dụ:

# Nhập số a: 1
# Nhập số b: 2
# Nhập số c: 3
# [1 2 3] là dãy tăng dần

# def check_arr(a, b, c):
#     if a > b > c:
#         print(f"[{a}, {b}, {c}] là dãy giảm dần")
#     elif a < b < c:
#         print(f"[{a}, {b}, {c}] là dãy tăng dần")
#     else:
#         print(f"[{a}, {b}, {c}] không phải dãy giảm dần, không phải dãy tăng dần")

# a = int(input("Nhập vào số a: "))
# b = int(input("Nhập vào số b: "))
# c = int(input("Nhập vào số c: "))

# check_arr(a, b, c)

# 5. Viết chương trình yêu cầu nhập một ký tự, kiểm tra và in ra ký tự đó có thuộc bảng alphabet(a-zA-Z) hay không

# Ví dụ:

# Nhập một ký tự: g
# 'g' thuộc bảng ký tự alphabet

# def char_check(char):
#     return "a" <= char.lower() <= "z"


# print(char_check(input("Nhap mot ky tu bat ky: ")))

# 6. Viết chương trình yêu cầu nhập một tháng trong năm, kiểm tra và in ra mùa tương ứng

# Ví dụ:

# Nhập một tháng bất kỳ: 5
# Tháng 5 là mùa hè


# def check_season(month):
#     season = "mùa xuân" if 1 <= month <= 3 else "mùa hè" if 4 <= month <= 6 else "mùa thu" if 7 <= month <= 9 else "mùa đông" if 10 <= month <= 12 else None

#     if season:
#         print(f"Tháng {month} là {season}")
#     else:
#         print(f"Tháng không hợp lệ")


# check_season(int(input("Nhập một tháng bất kỳ: ")))

# 7. Viết chương trình yêu cầu nhập một số, in ra bảng cửu chương của số đó

# Ví dụ:

# Nhập một số(1 - 9): 5
# 5 x 1 = 5
# 5 x 2 = 10
# ...

# def bcc(a):
#     if 1 <= a <= 9:
#         print(f"Bang cuu chuong cua {a} la: ")
#         for i in range(1, 11):
#             print(f"{a}  x {i:2} = {a*i:2}")


# bcc(int(input("Nhap mot so a tu 1 den 9: ")))

# 8. Viết chương trình yêu cầu nhập một số nguyên dương n, kiểm tra các số trong khoảng từ 1 - n
# - Nếu số chia hết cho 3 in ra Fizz
# - Nếu số chia hết cho 5 in ra Buzz
# - Nếu số chia hết cho 3 và 5 in ra FizzBuzz
# - Nếu không chia hết cho cả 3 và 5 in ra số đó

# Ví dụ:

# Nhập một số nguyên dương: 10
# 1
# 2
# Fizz
# 4
# Buzz
# ...

# def fizzbuzz(n):
#     for i in range(1, n + 1):
#         print("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i %
#               3 == 0 else "Buzz" if i % 5 == 0 else i)


# fizzbuzz(20)
# 9. Viết chương trình yêu cầu người dùng nhập số nguyên dương n tính tổng tất cả các số chia hết cho 3 và 5 trong khoảng từ 1 -> n


# def sum_to_n(n):
#     total = 0

#     for i in range(1, n + 1):
#         total += i if check_div(i) else 0

#     return total


# print(sum_to_n(30))

# 10. Viết chương trình yêu cầu người dùng nhập một loạt số, tính và in ra trung bình cộng của các số đó
# - Cho phép nhập số lượng số bất kỳ
# - In ra kết quả ngay lập tức với mỗi số nhập vào
# - Dừng nhập và in ra kết quả khi người dùng nhập 'q' hoặc 'c'

# Ví dụ:

# Nhập một số: 2
# Dãy số đã nhập: 2
# Trung bình cộng các số: 2.0
# Nhập một số: 5
# Dãy số đã nhập: 2 5
# Trung bình cộng các số: 3.5
# ...
# Nhập một số: q
# Exit!

# def avg_multiple():
#     total = 0
#     count = 0
#     list_of_numbers = ""

#     while True:
#         number = input("Enter a number: ")

#         if number.lower() == 'q' or number.lower() == 'c':
#             print("Exit")
#             return total / count
#         else:
#             count += 1
#             total += int(number)
#             list_of_numbers += " " + number
#             print(f"List of numbers: [{list_of_numbers} ]")
#             print(f"Average of numbers: {total / count}")


# print(avg_multiple())

# def to_km(value, unit):
#     if unit == "km":
#         return value
#     elif unit == "m":
#         return value * 10 ** -3
#     elif unit == "dm":
#         return value * 10 ** -4
#     elif unit == "cm":
#         return value * 10 ** -5
#     elif unit == "mm":
#         return value * 10 ** -6


# def sum(value1, unit1, value2, unit2):
#     total = to_km(value1, unit1) + to_km(value2, unit2)

#     if unit1 == "km":
#         return (total, "km")
#     elif unit1 == "m":
#         return (total * 10 ** 3, "m")
#     elif unit1 == "dm":
#         return total * 10 ** 4
#     elif unit1 == "cm":
#         return total * 10 ** 5
#     elif unit1 == "mm":
#         return total * 10 ** 6

# def is_prime(n):
#     return not (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0)

# 1. Viết chương trình gợi ý người dùng nhập một dãy số tùy ý (phân tách bằng dấu cách), lưu vào một list. Sắp xếp list số đã nhập, sau đó, tìm và hiển thị số lớn thứ 3 (Lưu ý trường hợp nhiều số trùng nhau)

# class Student:
#     _name = None
#     _roll = None

#     def __init__(self, name, roll) -> None:
#         self._name = name
#         self._roll = roll

#     def _display_roll(self):
#         print("Roll: ", self._roll)


# s = Student("Ba", "LoL")

# print(s._name)


_str = "This is a common interview question"


def func(_str: str) -> tuple:
    """
    Hàm này tìm và trả về ký tự có số lần xuất hiện lớn nhất trong chuỗi
    """

    _dict = dict()

    for char in _str:
        if char != " ":
            _dict[char] = _dict[char] + 1 if char in _dict else 1

    return sorted(_dict.items(), key=lambda item: item[1]).pop()


print(func(_str))
