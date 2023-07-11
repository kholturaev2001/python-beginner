# writing/creating files in python

text = 'Yoooooooo!\nThis is some text\nMay Allah bless you!'

with open('test.txt', 'w') as file:
    file.write(text)

with open('test.txt', 'a') as file:
    file.write("\nThis is an appended text")