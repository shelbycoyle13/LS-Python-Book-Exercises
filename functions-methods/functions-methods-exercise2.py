# # Take a look at this code snippet:

# foo = 'bar'

# def set_foo():
#     foo = 'qux'

# set_foo()
# print(foo)

# # What does this program print? Why?

This program prints 'bar'. When set_foo() is called, nothing prints because there is no call to print in the function body for set_foo. When we run print(foo), it uses the foo variable that is outside of the function because foo = 'bar' is a global variable, whereas the foo = 'qux' is local and not accessible outside of set_foo.