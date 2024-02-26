gryffindor = 0; slytherin = 0; ravenclaw = 0; hufflepuff = 0

answer1 = int(input("Q1) Do you like Dawn or Dusk?\n 1) Dawn\n 2) Dusk\n"))
if answer1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer1 == 2:
    slytherin += 1
    hufflepuff += 1
else:
    print("Wrong Input")

answer2 = int(input("Q2) When I'm dead, I want people to remember me as:\n 1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold\n"))
if answer2 == 1:
    hufflepuff += 2
elif answer2 == 2:
    slytherin += 2
elif answer2 == 3:
    ravenclaw += 2
elif answer2 == 4:
    gryffindor += 2
else:
    print("Wrong Input")

answer3 = int(input("Q3) Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n"))
if answer3 == 1:
    slytherin += 4
elif answer3 == 2:
    hufflepuff += 4
elif answer3 == 3:
    ravenclaw += 4
elif answer3 == 4:
    gryffindor += 4
else:
    print("Wrong Input")

if gryffindor > slytherin and gryffindor > hufflepuff and gryffindor > ravenclaw:
    print("Gryffindor!!!") 
elif slytherin > gryffindor and slytherin > hufflepuff and slytherin > ravenclaw:
    print("Slytherin!!!")
elif hufflepuff > gryffindor and hufflepuff > slytherin and hufflepuff > ravenclaw:
    print("Hufflepuff!!!")
else:
    print("Ravenclaw!!!")