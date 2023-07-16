class Car:
    # `class` is a blueprint to create objects

    # objects can have some combinations of attributes and methods
    # attributes describe, what an object is/has, e.g. ...

    # company = None
    # model = None
    # year = None
    # color = None



    # objects can also have methods, i.e. what an object can do, e.g. ...

    def __init__(self, company, model, year, color):  # __init__(self): -  this a constructor in other programming languages
        self.company = company
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print('This ' + self.company + ' ' + self.model + ' is driving')

    def stop(self):
        print('This ' + self.company + ' ' + self.model + ' is stopped')
