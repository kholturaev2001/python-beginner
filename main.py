# # slicing = create a substring by extracting elements from another string
# #             indexing[] or slice()
# #             [start:stop:step]
#
# name = 'Bro Code'
#
# first_name = name[0:3]
#
# last_name = name[4:]
#
# funky_name = name[0:8:2]  # or
# funky_name_two = name[:2]  # or
#
# reversed_name = name[::-1]
#
# print(reversed_name)


website = 'https://instagram.com'

slice_url = slice(8, -4)

print(website[slice_url])
