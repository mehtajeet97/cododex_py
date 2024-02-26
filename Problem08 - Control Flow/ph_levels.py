# Input the pH value from User
pH = int(input("Enter the pH value. Kindly enter a value between 0 to 14 : "))

# Output based on pH value input
if pH > 7:
    print("Basic")
elif pH < 7:
    print("Acidic")
else:
    print("Neutral")
