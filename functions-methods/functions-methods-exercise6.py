# What does the following code print?

# def scream(words):
#     words = words + '!!!!'
#     return
#     print(words)

# scream('Yipeee')

This will return Yipeee!!!! but this doesn't get a chance to get printed because the return keyword is on the line before the call to print. Return terminates the function.