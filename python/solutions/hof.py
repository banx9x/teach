# Thêm tham số param ở đây
def getData(fn, param, dataList):

    newList = []
    for item in dataList:
        # ở đây gọi checkData, nó trả về hàm inner(param)
        # -> fn(intem, newList) -> inner
        # -> inner(param)
        fn(item, newList)(param)
    return newList


def checkData(value, listData):

    def inner(param):
        if value > param:
            listData.append(value)
    return inner


demoArray = [1, 2, 56, 78, 3]

n = int(input("Enter a number: "))

data = getData(checkData, n, demoArray)

print(data)


def getData(f_one, f_two):
    def container(func):
        def inner(param, data):
            new_list = []
            mapped_data = f_one(data)
            f_two(param, mapped_data, new_list)

            return new_list
        return inner
    return container


def f_one(data):
    for i in range(len(data)):
        data[i] *= 2

    return data


def f_two(param, data, new_list):
    for i in data:
        if i > param:
            new_list.append(i)


demo_list = [1, 2, 56, 78, 3]


@getData(f_one, f_two)
def check(param, data):
    print("Do nothing here 😉")


number = int(input("Enter a number: "))

data = check(number, demo_list)
print(data)  # [112, 156]
