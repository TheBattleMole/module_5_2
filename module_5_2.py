class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floors:
            print("Такого этажа не существует")
        else:
            for i in range(1,new_floor + 1):
                print(i)
    def __len__(self):
        return self.floors

    def __str__(self):
        return f" Название: {self.name}, количество этажей: {self.floors}"

h1 = House("Бурдж-Халифа", 163)
h2 = House("Хрущевка", 5)
print(h1)
print(h2)
print(len(h1))
print(len(h2))

