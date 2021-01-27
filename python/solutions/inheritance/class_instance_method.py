class Demo:
    # constructor
    def __init__(self) -> None:
        super().__init__()
    # class method

    # decorator
    @classmethod
    def default(cls):  # factory
        return cls()

    # instance method
    def greet(self):
        print("LoL")


demo = Demo.default()
demo.greet()
