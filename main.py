print('''
*****************************************************************
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
*****************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

choice_1 = input("You are the beginning of your wonderful journey. You have two pathways to choose from. Left or Right Matey?\n").lower()
if choice_1 == "left":
 print("You have chosen the right path. You are now on the next stage of your journey.")
 choice_2 = input("You have come across a river. Do you want to swim or wait for the boat?\n").lower()
 if choice_2 == "swim":
    print("Your quick thinking has saved you. Proceed young lad.")
    choice_3 = input("Final step young buck. There are three doors, one as red as Captain Hook's eyes, one as blue as Pan's eyes, and one as yellow as Tinker's dress. Which door do you choose?\n").lower()

    if choice_3 == "red":
        print("You have chosen the wrong door. You have been burned by fire. Game over.")
    elif choice_3 == "blue":
        print("You have chosen the wrong door. You have been eaten by beasts. Game over.")
    elif choice_3 == "yellow":
        print("Ayeee congrats matey. You have found the treasure. You win!")
    else:
        print("You chose a door that does not exist.")
 else:
        print("You were beaten to the treasure by the British. Game Over.")
else:
        print("You have chosen the wrong path and are now dead. :(")

