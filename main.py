# exception =   events detected during execution that interrupt the flow of a program

try:
    numerator = int(input('Enter a number to divide: '))
    dominator = int(input('Enter a number to divide by: '))
    result = numerator / dominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print('You can not divide by zero! idiot!')
except ValueError as e:
    print(e)
    print('Enter only numbers plz!')
except Exception as e:
    print(e)
    print('Something went wrong :(')

else: print(str(result) + ' this is else statement')
finally:
    print("This will always execute")