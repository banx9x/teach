# Python không hỗ trợ nạp chồng phương thức
# Sử dụng module Multiple Dispatch Decorator
# pip3 install multipledispatch

from multipledispatch import dispatch


@dispatch(int, int)
def sum(a, b):
    return a + b


@dispatch(int, int, int)
def sum(a, b, c):
    return a + b + c


print(sum(1, 2, 3))
