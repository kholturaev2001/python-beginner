# *args =   parameter that will pack all arguments of a function into a tuple
#           useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0;
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1, 2, 3, 5,2, 5))