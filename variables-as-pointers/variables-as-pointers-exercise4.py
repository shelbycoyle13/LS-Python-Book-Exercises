# Without running this code, what will it print? Why?

# dict1 = {
#     'a': [1, 2, 3],
#     'b': (4, 5, 6),
# }

# dict2 = dict(dict1)
# dict1['a'][1] = 42
# print(dict2['a'])

When printing the last line in this code, 'a' in dict2 will still have the value as [1, 42, 3]

Dict2 is equal to a shallow copy of dict1. The dict() function makes shallow copies. So when we try and reference a list in a dictionary, the list has its own memory address. Regardless if changing from dict1 or dict2, they are both pointing to the same list.

When making a shallow copy of a dictionary, you're really just making a copy of the dictionary, but not the keys or values inside. This means the original dictionary and the shallow copy would point to the same keys and values.
