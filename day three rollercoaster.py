print("Welcome to the rollercoaster!")
height= int(input("What is your height?\n"))
if height >120:
    print("You can ride on the rollercoaster.")
    age = int(input("What is your age?"))
    bill = 0
    if age <12:
        bill+=5
        print("You have to pay $5 for your ticket.")
    elif age <=18:
        bill+=7
        print("You have to pay $7 for your ticket.")
    elif age >= 45 and age <=55:
        print("Everythings going to be okay, you got a free ride.")
    else:
        bill+=12
        print("You have to pay $12 for your ticket.")
    
        
    wants_photo=input("Do you want a photo? Y or N ")
    if wants_photo =="Y":
        bill+=3
    print(f"Your total bill is ${bill}")
else:
    print("Sorry you have to grow taller to get a ride.")