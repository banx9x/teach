class Product:
    def __init__(self, price) -> None:
        super().__init__()
        # 'ẩn' thuộc tính -> _Product__price
        # vẫn có thể truy cập và sửa đổi trực tiếp giá trị
        self.__price = price

    # getter
    @property
    def price(self):
        return self.__price

    # setter
    # nếu không có setter, sẽ không thể set giá trị cho thuộc tính
    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        else:
            self.__price = price


product = Product(10)
print(product.price)
product.price = 20
print(product.price)
product.price = -10

print(product._Product__price)
product._Product__price = 10
print(product.price)