# # -->> List - Array - Ordered collection of values, mutable

numbers = [13, 2, 23, 53, 13]
# # print(numbers[3]) # Index 3 
# # print(numbers[-1]) # Negative indexing 

# # numbers[2] = 17 # Changes index 2 value
# # print(numbers)

# # numbers[5] = 72 # Index cannot be accessed: out of range
# # print(numbers)

# # numbers.append(42) # Adding a value using a method, single values only
# # print(numbers)

# # numbers.insert(3, 20) # Insert 20 before index 3
# # print(numbers)

# numbers.pop() # Remove and return last index(default last)
# popped_value = numbers.pop(2)
# print(numbers)
# print(popped_value)

# numbers.remove(13)
# print(numbers)

# numbers.sort() # Default ascending
# numbers.sort(reverse=True) # Keyword argument
# print(numbers)

# print(numbers.count(13)) # Occurences of 13

# -->> Tuple - Ordered collection of values - immutable
names = ("Jane", "Martha", "Eugene", "Jacob", "Eugene")
# print(type(names))

# print(names[1]) # Index
# names[2] = 'Somebody' # Does not support item assignment

# print(names.index('Eugene')) # Index output -only first occurence if there's multiples
# print(names.index(6)) # Value error if index doesn't exist 
# print(len(names)) # Number of names in tuple
