# Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer.

def even_or_odd(number):
    if number % 2 == 0:
        print('This is an even number')
    else:
        print('This is an odd number')

get_number = int(input('Please provide a number: '))

even_or_odd(get_number)
