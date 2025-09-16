# Functions - A reusable collection of code that performs a particular task
# Declare a function
def greet(name, age, country='Australia'):
    print(f'Hello, {name}! You are {age} years old')
    print(f'{name} lives in {country}')

# Call the function. 
greet(name='Otieno', age=20)
greet('Jane', 21, 'Mexico') 

