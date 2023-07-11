
# str.format() =    optional method that gives users more control when displaying output

name = 'Muhammadrasul'
#
print('Hello, my name is {}'.format(name))
print('Hello, my name is {:<10}. Nice to meet you'.format(name))     # right padding
print('Hello, my name is {:>10}. Nice to meet you'.format(name))     # left padding
print('Hello, my name is {:^10}. Nice to meet you'.format(name))     # center