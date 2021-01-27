# Viết chương trình chuyển đổi một số nguyên thành một giá trị hex tương ứng
# VD: 255 -> ff
try:
    n = int(input("Enter a number: "))
    n = f"{n:0x}"
    print(f"Hex value: {n}")
except ValueError:
    print("Invalid number!!!")
