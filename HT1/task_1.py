# 1. Сreate a class hierarchy of animals with at least 5 animals that have additional methods each, create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class
# class Animals:
#  """
# Parent class, should have eat, sleep
# """
#
# class Animal1(Animal):
# """
# Some of the animal with 1-2 extra methods related to this animal


class Animal:

    def __init__(self, animal_cast, animal_name):
        self.cast = animal_cast
        self.name = animal_name

    def eat(self):
        print(self.cast + ' is called ' + self.name + ' like to eat.')

    def walk(self):
        print(self.cast + ' is called ' + self.name + ' like to walk.')

    def sleep(self):
        print(self.cast + ' is called ' + self.name + ' like to sleep.')


class Parrot(Animal):

    def speak(self):
        print(self.cast + ' is called ' + self.name + 'can speak.')

    def fly(self):
        print(self.cast + ' is called ' + self.name + 'can fly.')


class Snake(Animal):

    def creep(self):
        print(self.cast + ' is called ' + self.name + ' can creep.')

    def hiss(self):
        print(self.cast + ' is called ' + self.name + ' can hiss.')


class Frog(Animal):

    def jump(self):
        print(self.cast + ' is called ' + self.name + ' can jump.')

    def swim(self):
        print(self.cast + ' is called ' + self.name + ' can swim.')


class Spider(Animal):

    def web(self):
        print(self.cast + ' is called ' + self.name + ' can cobweb.')

    def climb_walls(self):
        print(self.cast + ' is called ' + self.name + ' can climb on the walls.')


class Raccoon(Animal):

    def wash(self):
        print(self.cast + ' is called ' + self.name + ' like wash everything.')


parrot = Parrot('Blue Ara', 'Rio')
snake = Snake('Anakonda', 'Kaa')
frog = Frog('Marsh frog', 'Pepa')
spider = Spider('Araneus', 'Otto')
raccoon = Raccoon('Procyon lotor', 'Rocket')


parrot.fly()
parrot.speak()

snake.creep()
snake.hiss()

frog.jump()
frog.swim()

spider.web()
spider.climb_walls()

raccoon.wash()
