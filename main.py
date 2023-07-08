# set = collection which is unordered, unindexed. No duplicate values

utensils = {'fork', 'spoon',  'knife'}
dishes = {'bowl', 'plate', 'cup', 'knife'}

# utensils.add('napkin')
# utensils.remove('fork')
# utensils.clear()
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)

# print(dishes.difference(utensils))
print(utensils.intersection(dishes)) # what element do these sets have in common

# for x in dinner_table:
#     print(x)