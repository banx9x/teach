# 1. Viết hàm find_min_max() cho phép nhập một số lượng "số nguyên dương" bất kỳ, in ra số lớn nhất, nhỏ nhất
# Dừng và in ra kết quả khi nhập 'q' hoặc 'c'
# Ví dụ:
# Enter number: 12
# Enter number: 15
# Enter number: 11
# Enter number: 8
# Enter number: 3
# Enter number: 21
# Enter number: q -> end, then print
# List of number: 12 15 11 8 3 21
# Largest number: 21
# Smallest number: 3
# Lưu ý không sử dụng list, tuple, ... và các phương thức math.min(), math.max()
# Gợi ý: sử dụng vòng lặp while


def find_min_max():
    number = input("Enter number: ")

    if number.lower() == 'q' or number.lower() == 'c':
        return

    min = max = int(number)
    list_of_number = number

    while True:
        number = input("Enter number: ")

        if number.lower() == 'q' or number.lower() == 'c':
            break

        if max < int(number):
            max = int(number)

        if min > int(number):
            min = int(number)

        list_of_number += " " + number

    print("List of numbers: " + list_of_number)
    print(f"Largest number: {max}")
    print(f"Smallest number: {min}")


# find_min_max()
# 2. Viết hàm print_fibonacci(n) in ra n số trong dãy fibonacci. Mặc định số thứ nhất và 2 là 0 1
# Ví dụ print_fibonacci(10)
# 0 1 1 2 3 5 8 13 21 34

# 3. Viết hàm print_pattern() in ra theo mẫu sau
# 1  2  3  4  5  6  7  8  9 10
# 2  4  6  8 10 12 14 16 18 20
# 3  6  9 12 15 18 21 24 27 30
# ...
def print_pattern():
    for i in range(1, 11):
        s = ""
        for j in range(1, 11):
            s += f"{i * j:3}"

        print(s)


# print_pattern()
# 4. Viết hàm is_leap_year(year) kiểm tra xem một năm có phải năm nhuận hay không, kết quả trả về là True hoặc False, lưu ý về các trường hợp của năm nhuận


def is_leaf_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


# print(is_leaf_year(2020))
# print(is_leaf_year(2000))
# print(is_leaf_year(2100))


# 5. Viết hàm tìm nghiệm phương trình bậc 2 ax^2 + bx + c = 0, hàm nhận 3 tham số a, b, c, in ra nghiệm phương trình, lưu ý điều kiện phương trình

# 6. Viết hàm kiểm tra một số có phải số nguyên tố hay không, kết quả trả về True hoặc False


# 7. Viết hàm in ra chữ số đầu và cuối của một số, VD: 12345 -> 15

def func(n):
    s = str(n)
    return s[0] + s[-1]


print(func(123434))


def func(n):
    last = n % 10
    first = None

    while n != 0:
        first = n % 10
        n //= 10

    return f"{first}{last}"

# func(123), n = 123
# last = 123 % 10 = 3
# fist = None
# n != 0 (n = 123) -> True
# first = n % 10 = 123 % 10 = 3
# n //= 10 -> n = 12
# n != 0 (n = 12) -> True
# first = n % 10 = 12 % 10 = 2
# n //= 10 -> n = 1
# n != 0 (n = 1) -> True
# first = n % 10 = 1 % 10 = 1
# n //= 10 -> n = 0
# n != 0 (n = 0) -> False
#
# first = 1, last = 3


print(func(4512324))

# 8. Viết hàm kiểm tra một số có phải số Strong hay không (? Số Strong là số có tổng giai thừa các chữ số bằng chính nó). VD: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145


# 9. Viết hàm print_number_pattern(n) in ra theo mẫu sau
# VD: n = 5
#  1
#  2  1
#  3  2  1
#  4  3  2  1
#  5  4  3  2  1


# 10. Viết hàm convert_temperature(temp, from, to) chuyển đổi nhiệt độ từ thang 'from' sang thang 'to'
# VD: convert_temperature(30, 'C', 'F') -> chuyển đổi nhiệt độ từ 30*C -> *F
# 3 thang nhiệt Celcius, Farenheit, Kevin

# 11. Viết hàm tính và trả về kết quả của phép trừ giữa tích và tổng tất cả chữ số của một số
# VD: 123 -> 1 * 2 * 3 - (1 + 2 + 3) = 0


# 12. Viết hàm is_triangle(a, b, c) nhận vào tham số là 3 cạnh của tam giác, kiểm tra xem độ dài 3 cạnh có tạo thành tam giác hợp lệ hay không, kết quả trả về True hoặc False
# VD: is_triangle(1, 2, 4) -> True

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


print(is_triangle(1, 2, 3))

# 13. Viết nearest(a, b) kiểm tra và trả về số gần với 100 nhất
# VD: nearest(105, 99) -> 99


def nearest(a, b):
    return a if abs(100 - a) <= abs(100 - b) else b


print(nearest(105, 99))
# 14. Viết hàm sum(value1, unit1, value2, unit2) nhận vào 2 tham số value1 và value2 là giá trị độ dài, unit1 và unit2 là đơn vị độ dài. Quy đổi giá trị unit2 về cùng đơn vị với unit1, tính và in ra tổng giá trị
# VD: sum(1, 'km', 100, 'm') -> 1.1 km


def to_km(v, u):
    u = u.lower()

    if u == 'km':
        return v
    elif u == 'm':
        return v * 10 ** -3
    elif u == 'dm':
        return v * 10 ** -4
    elif u == 'cm':
        return v * 10 ** -5
    elif u == 'mm':
        return v * 10 ** -6


def sum(v1, u1, v2, u2):
    sum = to_km(v1, u1) + to_km(v2, u2)

    u1 = u1.lower()

    if u1 == 'km':
        return sum, 'km'
    elif u1 == 'm':
        return sum * 10 ** 3, 'm'
    elif u1 == 'dm':
        return sum * 10 ** 4, 'dm'
    elif u1 == 'cm':
        return sum * 10 ** 5, 'cm'
    elif u1 == 'mm':
        return sum * 10 ** 6, 'mm'


print(sum(1, 'm', 10, 'mm'))
print(sum(1, 'km', 100, 'm'))
print(sum(1, 'mm', 10, 'cm'))



