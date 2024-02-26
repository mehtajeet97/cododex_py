# Entire lyrics of 99 bottles through this for-loop
for i in range(99, 0, -1):
    if i == 1:
        print(f'{i} bottle of beer on the wall\n{i} bottle of beer\nTake one down, pass it around')
    else:
        print(f'{i} bottles of beer on the wall\n{i} bottles of beer\nTake one down, pass it around')