# nested loops    =   one loop inside of another loop, i.e. The "inner loop" will finish all of its iterations
#                     before finishing one interation of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input('Enter a symbol to use: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()