# Explain why the code below prints different values on lines 3 and 4.

# text = "It's probably pining for the fjords!"

# print(text[21:35].rfind('f'))     # 8
# print(text.rfind('f', 21, 35))    # 29

The first print statement slices the string first and then reassigns new index numbers to the new slice. Then it returns the index number of where that character is first found, from right to left.

The second print statement just looks at the current indexes we are passing through in the rfind method, then returns the index number of where that character is first found, from right to left.