# Input height
height = int(input("What is your Height in cms : "))
# Input Credit
credit = int(input("How many credits do you have : "))

# Output based on conditions met
if height > 137 and credit > 10:
    print("Enjoy the ride!")
elif height < 137 and credit > 10:
    print("You are not tall enough to ride.")
elif height > 137 and credit < 10:
    print("You don't have enough credits.")
else:
    print("You do not meet either of the requirements.")