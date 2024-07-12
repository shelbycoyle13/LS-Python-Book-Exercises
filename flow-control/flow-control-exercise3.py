# Without running the following code, what does it print? Why?

# def bar_code_scanner(serial):
#     match serial:
#         case '123':
#             print('Product1')
#         case '113':
#             print('Product2')
#         case '142':
#             print('Product3')
#         case _:
#             print('Product not found!')

# bar_code_scanner('113')
# bar_code_scanner(142)

This will print Product2 and Product not found! '113' is a match in one of the cases, but since the second argument 142 isn't wrapped with single quotations, it doesn't match any of the cases, so it prints the default.