print("Welcome to Pyhton Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
#my code
# S == 15
# M == 20
# L == 25
# code for small
# small_P = 15
# large_P = 25
# med_P = 20
# if size == "S":
#     small_P =15
#     if add_pepperoni == "Y":
#         small_P += 2
#     if extra_cheese =="Y":
#         small_P += 1
# 
#     print(f"Your final bill is ${small_P}.")
# 
# 
# # Code for medium
# if size == "M":
#     med_P =20
#     if add_pepperoni == "Y":
#         med_P += 3
#     if extra_cheese =="Y":
#         med_P += 1
#     print(f"Your final bill is ${med_P}.")
# 
# # Code for large
# if size == "L":
#     large_P =25
#     if add_pepperoni == "Y":
#         large_P += 3
#     if extra_cheese =="Y":
#         large_P += 1
     print(f"Your final bill is ${large_P}.")


# Tutor's code    
bill =0 
if size =="S":
    bill= 15
elif size =="M":
    bill = 20
else:
    bill = 25
    
if add_perpperoni =="Y":
    if size =="S":
        bill+=2
    else:
        bill+=3
if extra_cheese == "Y":
    bill+=1

print(f"Your final bill is:{bill}.")