def closure():
    # biến cục bộ (function scrope)
    # không thể tham chiếu tới biến từ bên ngoài hàm
    var = 1

    def get():
        # tuy nhiên hàm get được khai báo bên trong closure
        # get có thể tham chiếu tới var
        # và ghi nhớ nó
        return var

    # khi gọi hàm closure
    # biến var được khởi tạo, cùng với hàm get
    # closure trả về hàm get
    # và bởi vì get có tham chiếu tới var
    # bởi vậy var vẫn còn tồn tại cho dù hàm closure đã kết thúc
    return get


demo = closure()  # demo = get

# print(var) # error
demo()  # get() -> var

print(demo())
