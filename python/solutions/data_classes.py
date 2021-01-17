from collections import namedtuple

# Thay thế cho các class chỉ dùng để chứa dữ liệu
# Tương tự tuple, namedtuple không thể thay đổi giá trị
# Nhưng không chứa các phương thức rác, chỉ chứa dữ liệu, và cũng không cần triển khai phương thức so sánh __eq__
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)

print(p1 == p2)
