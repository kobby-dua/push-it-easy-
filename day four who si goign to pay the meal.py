names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
Rnames = len(names)


import random
# gives the random person a number based on the arrrangement and number of persons inputed
no_Rand_person = random.randint(0, Rnames - 1)
Random_person = (names[no_Rand_person])

print(f"{Random_person} would be the one to pay the bill today.")

# 
# Random_person = random.choice(names)
# print(Random_person + " is going to pay the bill today.")