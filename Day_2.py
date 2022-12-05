from tkinter.filedialog import Open


file = open("2.txt")
lines = file.readlines()
total = 0
total2 = 0
# lose-0 draw-3 win-6
# A/X - 1
# B/Y - 2
# C/Z - 3

guide = {

    "A X\n": 4,   #draw
    "A Y\n": 8,   #win
    "A Z\n": 3,  #loss
    "B X\n": 1,  #loss
    "B Y\n": 5,   #draw
    "B Z\n": 9,   #win
    "C X\n": 7,   #win
    "C Y\n": 2,  #loss
    "C Z\n": 6    #draw
}

guide2 = {

    "A A\n": 4,   #draw
    "A B\n": 8,   #win
    "A C\n": 3,  #loss

    "B C\n": 1,  #loss
    "B B\n": 5,   #draw
    "B A\n": 9,   #win

    "C B\n": 7,   #win
    "C A\n": 2,  #loss
    "C C\n": 6    #draw
}

conditions = {
    "A X\n": "A C\n",
    "A Y\n": "A A\n",
    "A Z\n": "A B\n",
    "B X\n": "B C\n",
    "B Y\n": "B B\n",
    "B Z\n": "B A\n",
    "C X\n": "C A\n",
    "C Y\n": "C C\n",
    "C Z\n": "C B\n"
}

for line in lines:
    # total+= int(guide[line]),
    total2+= guide2[conditions[line]]

print("Total score for part 1 is: " + str(total))
print("Total score for part 2 is: " + str(total2))

   

