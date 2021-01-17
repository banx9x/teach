def odd():
    for i in range(1, 999, 2):
        yield i


sequense = odd()  # tạo một object

print(next(sequense))  # 1

print(next(sequense))  # 3
