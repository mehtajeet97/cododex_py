print('BANK OF CODÉDEX')

# Input pin from user
pin = int(input('Enter your PIN: '))

# Keep asking for the PIN until the user guesses it correctly
while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

# User inputs correct PIN
if pin == 1234:
  print('PIN accepted!')