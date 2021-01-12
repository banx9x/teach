# Viết chương trình chuyển đổi một số nguyên thành một binary list tương ứng
# VD: 10 -> [1, 0, 1, 0]
try:
    n = int(input("Enter a number: "))
    b = [int(i) for i in f"{n:0b}"]
    print(f"Binary list: {b}")
except ValueError:
    print("Invalid number!!!")
