# Loop from 1 to 100 including both
for i in range(1,101,1):
# First condition checks for both
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
# Second condition checks only for 3
    elif i%3 == 0:
        print("Fizz")
# Third condition checks only for 5
    elif i%5 == 0:
        print("Buzz")
# Print the number
    else:
        print(f'{i}')