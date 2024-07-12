# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')

# Note: this problem is a bit tricky.

turn_into_list = list(stuff)

turn_into_list[2] = 'goodbye'

back_to_tuple = tuple(turn_into_list)

print(back_to_tuple)

