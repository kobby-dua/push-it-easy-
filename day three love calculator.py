print("Welcome to the Love calculator!")
name1=input("What is your name? \n").lower()
name2=input("What is thier name? \n").lower()

# name 1
T=int(name1.count("t"))
r=int(name1.count("r"))
u=int(name1.count("u"))
e=int(name1.count("e"))
true = (T+r+u+e)

L=int(name1.count("l"))
o=int(name1.count("o"))
v=int(name1.count("v"))
e=int(name1.count("e"))
Love = (L+o+v+e)

First_P= str(true+Love)



# name 2
L=int(name2.count("l"))
o=int(name2.count("o"))
v=int(name2.count("v"))
e=int(name2.count("e"))
Love = (L+o+v+e)

T=int(name2.count("t"))
r=int(name2.count("r"))
u=int(name2.count("u"))
e=int(name2.count("e"))
true = (T+r+u+e)

Second_P = str(true +Love)
Love_Score = int(First_P + Second_P)



if Love_Score <10 or Love_Score > 90:
    print(f"Your love score is {Love_Score}%, you go together like coke and mentos.")
elif Love_Score <50 and Love_Score >40:
    print(f"Your score is {Love_Score}%, you are alright togther.")
else :
    print(f"Your score is {Love_Score}%." )
