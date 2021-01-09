class VinUni:
    def __init__(self, ID, fname, lname, category) -> None:
        super().__init__()
        self.ID = ID
        self.fname = fname
        self.lname = lname
        self.category = category

    def disp_info(self):
        print(f"Name: {self.lname} {self.fname}")
        print(f"Category: {self.category}")


class Student(VinUni):
    def __init__(self, ID, fname, lname, category) -> None:
        super().__init__(ID, fname, lname, category)

    def disp_id(self):
        print(f"Student ID: {self.ID}")


class Staff(VinUni):
    def __init__(self, ID, fname, lname, category) -> None:
        super().__init__(ID, fname, lname, category)

    def disp_id(self):
        print(f"Staff ID: {self.ID}")


info = input("Enter Student/Staff Info (ID, fname, lname, category): ")

info = info.split(sep=",")
info = list(map(lambda i: i.strip(), info))

if info[3] == "Student":
    student = Student(info[0], info[1], info[2], info[3])
    student.disp_info()
    student.disp_id()
else:
    staff = Staff(info[0], info[1], info[2], info[3])
    staff.disp_info()
    staff.disp_id()
