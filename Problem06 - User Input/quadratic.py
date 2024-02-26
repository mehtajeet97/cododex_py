# Quadratic Equation : ax**2 + bx + c = 0 
# User Input for a
a = int(input('Enter the coffecient for x-square: '))
# User Input for b
b = int(input('Enter the coefficient for x: '))
# User Input for c
c = int(input('Enter the constant: '))
# Value of x by quadratic formula
x1 = (-b + (b**2 - 4*a*c)**0.5)/2*a
x2 = (-b - (b**2 - 4*a*c)**0.5)/2*a
# Output
print(x1, x2)