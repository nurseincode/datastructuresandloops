# Output if a number is prime
# 16 -> 1, 2, 4, 8, 16 -> not prime
# 17 -> 1, 17 -> prime

number = 17
for i in range(2, number):
    if number % i == 0:
        print('Not a prime')
        break
else:
    print('Is a Prime')
    
