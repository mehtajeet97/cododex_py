# Initiate guess, tries with zero
guess = 0; tries = 0

# Keep running until guess is 6 and tries is not 3
while guess != 6 and tries != 3 :
  guess = int(input("Guess the number:  "))
  tries += 1

# Checks if correctly guessed or out of tries
if guess == 6:
   print("You got it!")
else:
   print("You have reached maximum tries")