# Without running this code, what will it print? Why?

# set1 = {42, 'Monty Python', ('a', 'b', 'c')}
# set2 = set1
# set1.add(range(5, 10))
# print(set2)

# Don't worry about having an exact match for the output. The important part is to show something that accurately represents set2.

When you print set2, you will get the same set when you print set1. Both set1 and set2 point to the same set. When you make a change to set1, it will make the same change for set2 and vice versa. We are also dealing with sets, so the elements may not show up in the same order, but the same elements will appear when printing both set1 and set2.