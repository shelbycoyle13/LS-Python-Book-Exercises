# Using the code below, classify the identifiers as global, local, or built-in. For our purposes, you may assume this code is the entire program.

# def multiply(left, right):    #multiply = global; left and right are local
#     return left * right

# def get_num(prompt):          #get_num = global; prompt = local
#     return float(input(prompt))   #float and input are built-in

# first_number = get_num('Enter the first number: ')    #first_number = global
# second_number = get_num('Enter the second number: ')  #second_number = global
# product = multiply(first_number, second_number)       #product = global
# print(f'{first_number} * {second_number} = {product}')    #print = built-ins