# The following code causes an infinite loop (a loop that never stops iterating). Why?

# counter = 0

# while counter < 5:
#     print(counter)

The counter starts at 0. Then, we start the while loop. The first statement in the loop says "while the counter is less than 5, print the counter." The problem is the counter always stays at 0 because there are no other statements to edit the counter, to make it count up or any less. It always stays at 0, so it always fulfills the condition of the while loop, and thus always prints 0 in an infinite loop.