# method overriding = is the ability of an OOP language to allow a subclass (child class)
# to provide a specific implementation of a method that is already provided by one of its parents

class Animal:

    def eat(self): # in this case we want to override eat() method
        print('This animal is eating')

class Rabbit(Animal):

    def eat(self):
        print('This rabbit is eating a carrot')

rabbit = Rabbit()
rabbit.eat()