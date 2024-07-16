# Without running this code, what will it print? Why?

# dict1 = {
#     "Hitchhiker's Guide to the Galaxy": 42,
#     'Monty Python': 'The Life of Brian',
#     'Airplane!': "Don't call me Shirley!",
# }

# dict2 = dict(dict1)
# dict2['Monty Python'] = 'Holy Grail'
# print(dict1['Monty Python'])

Here we have dict1 and dict2. Dict2 makes another brand new dictionary that has the same elements as dict1. They are the same in value but they are two different objects. This is due to the dict() function.

When we make a change in dict2, we are only making a change in dict2. Thus, when printing the last statement for dict1, it prints out the original value 'Life of Brian'