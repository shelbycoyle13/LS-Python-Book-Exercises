# Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that obj references? Which statements do neither? If necessary, you can read the documentation.

# obj = 'ABcd'          #Reassign
# obj.upper()           #Neither
# obj = obj.lower()     #Reassign
# print(len(obj))       #Neither
# obj = list(obj)       #Reassign
# obj.pop()             #Mutate
# obj[2] = 'X'          #Mutate
# obj.sort()            #Mutate
# set(obj)              #Neither
# obj = tuple(obj)      #Reassign