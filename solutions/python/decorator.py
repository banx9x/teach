# Decorator là một hàm nhận tham số đầu vào là một hàm khác, decorator mở rộng tính năng cho hàm đó mà không làm thay đổi nội dung

def sum(a, b):
    return a + b


def min(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a - b


# operate nhận các hàm khác là tham số đầu vào
# và gọi hàm với tham số khác kèm theo
def operate(func, a, b):
    # có thể mở rộng chức năng cho hàm đầu vào ở đây
    print("Do something before call function")
    return func(a, b)


print(operate(sum, 2, 5))


# operate có thể trả về một hàm con
# nó chỉ nhận một hàm là tham số đầu vào
def operate(func):
    def inner(a, b):

        print("Do something before call function")
        # thay vì gọi và trả về kết quả trực tiếp trong operate
        # hàm được gọi bên trong hàm con (inner)
        return func(a, b)

    # trả về hàm inner, cho phép tái sử dụng
    return inner


op = operate(mul)  # op = inner
op(4, 3)  # inner(4, 3) -> func(4, 3) -> mul(4, 3) -> 12

print(op(4, 3))

# Python hỗ trợ cú pháp để đơn giản hóa việc phải gọi hàm operate thủ công
# Sử dụng @tên_hàm


@operate  # operate(sum)
def sum(a, b):
    return a + b


@operate  # operate(mul)
def mul(a, b):
    return a * b


print(sum(5, 5))


# Chuỗi decorator
# Đơn giản là các hàm lồng sâu hơn
def grand(func):
    def f(*args):
        print("Grand function")
        print("Grand function do something")
        return func(*args)

    return f


def parent(func):
    def f(*args):
        print("Parent function")
        print("Parent do something")
        return func(*args)

    return f


@grand
@parent
def sum(*args):
    print("Sum function")
    print("I'm calculate and return sum of values")
    result = 0
    for i in args:
        result += i

    return result


print(sum(1, 2, 3, 4, 5))


def loop(number: int = 1):
    def container(func):
        def inner(*args, **kwargs):
            for i in range(number):
                func(*args, **kwargs)
        return inner
    return container


@loop()
def greeting(name: str = "Stranger"):
    print(f"Hello, {name}")


greeting("Ba")
