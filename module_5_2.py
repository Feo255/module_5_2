class House:

    def __init__ (self, name, number_of_floors):
        new_floor = 0

        self.name = name
        self.number_of_floors =number_of_floors

    def __len__(self):

        return (self.number_of_floors)

    def __str__(self):
        str1 = None
        str2 = None
        str_summ = None
        str1 = 'Название: ' + str(self.name)
        str2 = ', кол-во этажей: ' + str(self.number_of_floors)
        str_summ = str1 + str2

        return (str_summ)





h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
