# dictionary =  A changeable/mutable, unordered collection of unique key:value pairs
#               Fast because they use hashing, allow us to access a value quickly

capitals = {
    'USA': 'Washington D.C.',
    'India': 'New Deli',
    'China': 'Beijing',
    'Russia': 'Moscow'
}

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'New York'})
capitals.pop('China')
# capitals.clear()

print(capitals['Russia'])
print(capitals['Germany'])
print(capitals.get('Germany'))  # this much safer way to check
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)