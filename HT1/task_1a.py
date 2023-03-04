# 1.a. Create a new class Human and use multiple inheritance to create Centaur class, create an instance of Centaur class and call the common method of these classes and unique.
#
#  class Human:
# """
# Human class, should have eat, sleep, study, work
# """
#
#  class Centaur(.. , ..):
# """
# Centaur class should be inherited from Human and Animal and has unique method related to it.
#  """


class Human:
    def eat(self):
        print("Human is eating.")

    def sleep(self):
        print('Human is sleeping.')

    def study(self):
        print('Human is studying.')

    def work(self):
        print('Human is working.')


class Animal:
    def run(self):
        print('Animal is running.')

    def feel_odors(self):
        print('Animal is feel odors.')


class Centaur(Human, Animal):
    def __init__(self, name_centaur):
        self.name = name_centaur

    def combination_qualities(self):
        print('Centaur ' + self.name + ' is galloping.')


centaur = Centaur('Odin')

centaur.eat()
centaur.sleep()
centaur.study()
centaur.work()
centaur.run()
centaur.feel_odors()

centaur.combination_qualities()
