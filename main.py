# method chaining = is used to call multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print('You start the engine')
        return self

    def drive(self):
        print('You drive the engine')
        return self

    def brake(self):
        print('You step the brakes')
        return self

    def turn_off(self):
        print('You turn off engine')
        return self

car = Car()

# car.turn_on().drive()
# car.brake().turn_off()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()