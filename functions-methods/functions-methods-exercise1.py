# What happens when you run the following program? Why do we get that result?

# def set_foo():
#     foo = 'bar'

# set_foo()
# print(foo)

When set_foo() is called, nothing prints because there were no calls to print in the function definition. When print(foo) tries to run, an error appears because foo is not in the outer scope, it only lives inside the set_foo function, therefore, it cannot be accessed outside of the function.