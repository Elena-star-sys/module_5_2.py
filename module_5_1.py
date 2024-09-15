class House:
    def __init__(self,name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor +1):
                print(floor)
        else:
            print('Такого этажа не существует')

    def __str__(self):
        return f"Название: {self.name} , количесвто этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))
