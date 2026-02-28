print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You're at a crossroad. Where would you like to go? \n Left or Right \n")

if direction == "Left":
    print("\nYou have come to a lake and you can see an island in the middle of the lake")
    print("Would you like to swim? Or Would you like to wait for a boat")
    lake_place = input("Type swim to 'Swim' or type 'Wait' to wait for a boat: ")
    if lake_place == "Wait":
        print("\nThe Boat has Arrived!")
        print("Going to the island")
        print("You have arrived on the island but now you see three doors.")
        print("Door Blue, Yellow and Red. Which would you like to pick? \n")
        door = input("Type 'Red' to choose the red door \n"
                     "Type 'Blue' to choose the blue door \n"
                     "Type 'Yellow' to choose the yellow door: ")
        if door == "Blue":
            print("You got eaten by the beast behind the Blue door")
            print("Game Over")
        elif door == "Red":
            print("Behind the red door were flames, you were burned alive")
            print("Game Over")
        elif door == "Yellow":
            print("\nCongratulations!!")
            print("You found the treasure!")
        else:
            print("\nYou did not pick any door")
            print("You've lost")
    else:
        print("You were attacked by trout")
        print("Game Over")
else:
    print("Fell into a hole.")
    print("Game Over")