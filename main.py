from car import Car

car_1 = Car('Mercedes', 'S-Class', 2022, 'black')
car_2 = Car('Toyota', 'Camry', 2019, 'white')

# Car.wheels = 3  # it changes all instances of a class
car_1.wheels = 6

print(car_1.wheels)
print(car_2.wheels)
print(Car.wheels)

