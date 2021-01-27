# Viết chương trình tạo mã màu hex ngẫu nhiên
from random import randint


def random_hex():
    r = randint(0, 255 ** 3)
    return f"{r:0x}"

print(random_hex())
print(random_hex())
