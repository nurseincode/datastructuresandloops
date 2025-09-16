def add(num1, num2):
    # sum = num1 + num2
    # return sum

# Optimize above
    return num1 + num2
  

# total = add(10, 20)
# final = add(total, 90) # Add 'total' and third value 
# print(final) # Add 'total' and 'final'

# Function calls for optimization - saves memory, speed(e.g in complex progs w loops+++, every sec adds up)

final = add(add(10, 20), 90) 
print(final) 
