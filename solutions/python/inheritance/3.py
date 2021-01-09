class Family:
    count = 0

    def __init__(self, son_name, father_name, mother_name) -> None:
        super().__init__()
        self.son_name = son_name
        self.father_name = father_name
        self.mother_name = mother_name

    def __str__(self) -> str:
        return f"-------Family No.{Family.count + 1}-------"


class Father(Family):
    def show_father(self):
        print(
            f"Father's Name: {self.father_name} ({self.father_age}-year-old)")


class Mother(Family):
    def show_mother(self):
        print(
            f"Mother's Name: {self.mother_name} ({self.mother_age}-year-old)")


class Son(Father, Mother):
    def __init__(self, son_name, son_age, father_name, father_age, mother_name, mother_age) -> None:
        super().__init__(son_name, father_name, mother_name)
        self.son_age = son_age
        self.father_age = father_age
        self.mother_age = mother_age

    def show_parrent(self):
        self.show_father()
        self.show_mother()

    def show_son(self):
        print(f"Son's Name: {self.son_name} ({self.son_age}-year-old)")

    def __str__(self) -> str:
        return super().__str__()


num_of_families = int(input("Enter number of families: "))

for i in range(num_of_families):
    s = input(
        "Enter Family Info (son_name, son_age, father_name, father_age, mother_name, mother_age): ")
    s = s.split(sep=",")
    s = list(map(lambda i: i.strip(), s))

    son = Son(s[0], s[1], s[2], s[3], s[4], s[5])
    print(son)
    son.show_son()
    son.show_parrent()

    Family.count += 1
