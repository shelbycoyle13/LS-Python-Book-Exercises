# What does the following function do? Be sure to identify the output value.

# def do_something(dictionary):
#     return sorted(dictionary.keys())[1].upper()

# my_dict = {
#     'Karl':     108,
#     'Clare':    175,
#     'Karis':    140,
#     'Trevor':   180,
#     'Antonina': 132,
#     'Chris':    101,
# }

# print(do_something(my_dict))

When running the print statement, this will print out CHRIS. 
We need to take this step by step.
First, we call dictionary.keys so we can see only the keys from the dictionary that are going to be passed into the do_something function. 
Then, sorted gets called, and sorts the keys alphabetically. 
Then, we look at index 1, which, after sorted, is Chris.
Finally, the upper method gets called, which returns a new string in uppercase letters, hence 'CHRIS'