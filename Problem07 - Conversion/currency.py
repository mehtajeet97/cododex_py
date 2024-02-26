# Cash remaining in Pesos (Columbia)
p = int(input('What do you have left in pesos?: '))
# Cash remaining in Soles (Peru)
s = int(input('What do you have left in soles?: '))
# Cash remaining in Reais (Brazil)
r = int(input('What do you have left in reais?: '))

# Total in dollars (based on conversion rates)
d = p * 0.00025 + s * 0.26 + r * 0.20

# Output
print(d)