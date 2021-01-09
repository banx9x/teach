class Student:
    lab_max = 80
    midterm_max = 60
    final_max = 70

    lab_rate = 0.3
    midterm_rate = 0.3
    final_rate = 0.4

    def __init__(self, name, lab, midterm, final) -> None:
        super().__init__()
        self.name = name
        self.lab = lab
        self.midterm = midterm
        self.final = final

    def cal_lab(self):
        return (self.lab / self.lab_max) * self.lab_rate * 100

    def cal_midterm(self):
        return (self.midterm / self.midterm_max) * self.midterm_rate * 100

    def cal_final(self):
        return (self.final / self.final_max) * self.final_rate * 100

    def cal_total(self):
        return self.cal_lab() + self.cal_midterm() + self.cal_final()

    def cal_grade(self):
        total = self.cal_total()

        if total < 50:
            return "F"
        if total < 60:
            return "D"
        if total < 70:
            return "B"
        return "A"

    def __str__(self) -> str:
        return f"{self.name:8}:  {self.cal_lab():.1f}    {self.cal_midterm():.1f}    {self.cal_final():.1f}   {self.cal_total():.1f}%   {self.cal_grade()}"


if __name__ == "__main__":
    list_of_students = []
    num_of_students = int(input("Enter number of Student: "))

    for i in range(num_of_students):
        s = input(
            f"Enter infomation for Student {i + 1} (Name, lab, midterm, final): ").split(sep=",")
        name = s[0].strip()
        lab = int(s[1])
        midterm = int(s[2])
        final = int(s[3])

        list_of_students.append(Student(name, lab, midterm, final))

    print("---------------Course Grade------------------")
    print("Name    :  Lab   Midterm  Final  Total  Grade")
    print("           (30%)  (30%)   (40%)  (100%)")
    for s in list_of_students:
        print(s)
    print("---------------------------------------------")
