# Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. Otherwise, it should return the original string. Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

string = str(input("Let's find out if this string will end up all uppercase. Please type something to me: "))

def all_caps_or_not(string):
    if len(string) > 10:
        print(string.upper())
    else:
        print(string)

all_caps_or_not(string)