# Without running the following code, what do you think it will do?

# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)

# foo(42, 3.141592)

This will print 42, 3.141592, 2. We provided 2 arguments and forgot a third. Luckily, there is a default value already set in place for the third argument, so because of that, we get 2 for that value.