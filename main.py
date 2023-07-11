import random

x = random.randint(1, 7)
y = random.random()

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

# shuffle random moduls
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", 'Q', 'M', '@']

random.shuffle(cards)

print(cards)