# What happens when you run the following code? Why?

# NAME = 'Victor'
# print('Good Morning, ' + NAME)
# print('Good Afternoon, ' + NAME)
# print('Good Evening, ' + NAME)

# NAME = 'Nina'
# print('Good Morning, ' + NAME)
# print('Good Afternoon, ' + NAME)
# print('Good Evening, ' + NAME)

This will print with Victor's name the first three statements, then it will print with Nina's name for the last three statements. Even though NAME is in all capital letters, indicating a constant variable, this is just for programmers to be aware of. Python doesn't actually have a way to prevent reassignment in a constant variable, hence why the value of name changes to Nina.

