from car import Car

car_1 = Car('Mercedes', 'S-Class', 2022, 'black')
car_2 = Car('Toyota', 'Camry', 2019, 'white')

# attributes
print(car_2.company)
print(car_2.model)
print(car_2.year)
print(car_2.color)

# methods
car_2.drive()
car_2.stop()