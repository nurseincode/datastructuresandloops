# Function to determine if a number is even or odd

def even_or_odd(num):
    if num % 2 == 0:
        return('Even')
    else:
        return('Odd')


print(even_or_odd(5))
result = even_or_odd(10) # Store value in variable 'result'
even_or_odd(2585) # Incomplete. Returns Odd but result not stored/printed
print(f'10 is {result}.') # Prints a message using the 'result' stored earlier