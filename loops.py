# print(1)
# print(2)
# print(3)
# print(4)
# print(5) # same result but not DRY

# -->> while loop
# number = 1
# while number <= 5:
#     print(number)
#     number += 1 # increment

# -->> For loop
# names = ["Jane", "Martha", "Eugene", "Jacob", "Eugene"]
         
# # for name in names: 
# #     print(name)

# for index, name in enumerate(names): # Loop over list for index and element together
#     print(f'{index+1}. {name}')

# List all numbers between 10 and 100, state if odd or even 
# for num in range(10,101): 
#     if num % 2 == 0:
#         print(f'{num} is even')
#     else:
#         print(f'{num} is odd')

# With ternary expression
for num in range(10, 101):
    # print(f'{num} is {'even' if num % 2 == 0 else 'odd'}')
    # print(f'{num} is {'odd' if num % 2 else 'even'}') --> refine further, however not as readable as above
