class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    edible = False
    pass


class Fruit(Plant):
    edible = True
    pass


class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):

    def eat(self, food):
        if food.edible == True:
            Animal.fed = True
            print(f'{self.name} съел {food.name}')

        else:
            Animal.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Predator(Animal):

    def eat(self, food):
        if food.edible == True:
            Animal.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            Animal.alive = False
            print(f'{self.name} не стал есть {food.name}')


a1 = Predator('Лев')
a2 = Mammal('Лось')
p1 = Flower('Роза')
p2 = Fruit('Яблоко')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
