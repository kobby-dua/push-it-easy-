print("Welcome to Treasure Island.")
print("Your mission here is to find the mystic treasure.")

choice1 = input("Where do you want to go, 'left' or 'right'? \n").lower()

if choice1 == 'left':
    choice2 = input('You\'ve come to a lake. There is an Island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        print("You arrived at the Island unharmed, but you were charged an amount of $10. There is a house with 3 doors. One 'red', one 'yellow' and one 'blue'. What colour do you choose? ")
        choice3 = input("Select a colour to open the door.\n")
        if choice3 == "yellow":
            print("Congratulations for finding the mystic treasure! YOU WIN!")
        elif choice3 =="blue":
            print("ouuuuuchhhhhh you entered the den of Lions. GAME OVER!")
        elif choice3 =="red":
            print("You cought fire. GAME OVER!")
        else:
            print(" you chose your own door . GAME OVER!")
        
    else: 
        print("Sorry, You've been eating by Crocodiles. GAME OVER!")
else:
    print("Sorry you fell into a hole. GAME OVER!")
     
    
#     
#     
# choice2 = input("Would you like to 'wait' or 'swim'? \n").lower
#     
#          
# 
# if choice2 =="wait":
#     print("You are before three great doors, of which an entry through 'one' of these unvails the mystic treasure.")
# else:
#     print("Sorry! You got eating by crocodiles. GAME OVER!")
#     
# choice3 = input("Do you want to go through the 'Red','Yellow' or 'Blue' door? \n")
# if choice3 == "Yellow":
#     print("Congratulations you found the treasure. YOU WIN!")
# elif choice == "Blue":
#     print("ooouucchhhh! You are on fire! GAME OVER!")
# else:
#     print("HoLy MoLy You entered a room full of lions! GAME OVER!")
# 
# 
#     
# 
# 
# 
# 
#     choice2 = input("You have reached a cross road.'wait' or 'swim'? \n").lower
# if choice2 =="wait":
#     choice3 = input("which door do you want to go through to find your treasure? 'Red','Yellow','Blue', \n").lower
#         
# else:
#     print("You fell into a hole Game over!")