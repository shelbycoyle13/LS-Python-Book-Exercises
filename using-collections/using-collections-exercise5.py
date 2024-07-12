# Which of the following values can't be used as a key in a dict object, and why?

# 'cat'                     #Yes
# (3, 1, 4, 1, 5, 9, 2)     #Yes
# ['a', 'b']                #No, lists are mutable
# {'a': 1, 'b': 2}          #No, dictionaries are mutable
# range(5)                  #Yes
# {1, 4, 9, 16, 25}         #No, sets are mutable
# 3                         #Yes
# 0.0                       #Yes
# frozenset({1, 4, 9, 16, 25})      #Yes