# INHERITANCE in python
# Classes can have children.

class Animal: # parent class

    alive = True

    def eat(self):
        print('This animal is eating')

    def sleep(self):
        print('This animal is sleeping')


class Rabbit(Animal): # this is a child class, and it inherits all what the Animal class has
    def run(self):
        print('This rabbit is running')
class Fish(Animal):
    def swim(self):
        print('This fish is swimming')
class Hawk(Animal):
    def fly(self):
        print('This hawk is flying')

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()

