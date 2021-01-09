class Product:
    def __init__(self, price) -> None:
        super().__init__()
        self.__price = price

    @property
    def price(self):
        return self.__price

    # nếu không có getter, sẽ không thể set giá trị cho thuộc tính
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
