class Apartment:
    apartment_name = "Sunshine Apartment"

    def __init__(self, tenant, block, floor, unit) -> None:
        super().__init__()
        self.tenant = tenant
        self.block = block
        self.floor = floor
        self.unit = unit
        self.rent = 0

    def __str__(self) -> str:
        return f"{self.tenant} staying at Block {self.block}, {self.floor}F-#{self.unit}, Monthly Rent ${self.rent:,.2f}"

    def assign_rent(self, monthly_rent):
        self.rent = monthly_rent


list_of_tenants = []
number_of_tenants = int(input("Enter number of tenants: "))

for i in range(number_of_tenants):
    s = input(
        f"Enter infomation for tenant {i + 1} (Name, block, floor, unit): ").split(sep=",")
    name = s[0].strip()
    block = s[1].strip()
    floor = int(s[2])
    unit = int(s[2])
    list_of_tenants.append(Apartment(name, block, floor, unit))

for i in list_of_tenants:
    monthly_rent = int(input(
        f"Enter the monthly rent for {i.tenant}: "))
    i.assign_rent(monthly_rent)

rents = [i.rent for i in list_of_tenants]


def avg(*args):
    result = 0
    for i in args:
        result += i

    return result / len(args)


print(f"Welcome to {Apartment.apartment_name}!")
for i in list_of_tenants:
    print(i)
print(f"The Average Monthly Rent is ${avg(*rents):,.2f}")
