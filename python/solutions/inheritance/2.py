class Person:
    def __init__(self, name, age, birth_place) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.birth_place = birth_place

    def birth_year(self):
        return 2021 - self.age

    def __str__(self) -> str:
        return f"Person: {self.name} was born in {self.birth_place} in {self.birth_year()}."


class Player(Person):
    def __init__(self, name, age, birth_place, gender) -> None:
        super().__init__(name, age, birth_place)
        self.gender = gender

    def __str__(self) -> str:
        return super().__str__() + f" {'She' if self.gender == 'F' else 'He'} is {self.age} years old this year."


i = input("Enter Player Info (Name, Age, Birth Place, Gender): ")

i = i.split(sep=", ")
i = list(map(lambda i: i.strip(), i))

person = Person(i[0], int(i[1]), i[2])
player = Player(i[0], int(i[1]), i[2], i[3])

print(person)
print(player)
