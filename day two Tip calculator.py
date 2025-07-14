print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n"))
percent_tip = float(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
number = int(input("How many people to split the bill?"))
percent_tip_to_share = (percent_tip/100)*(bill)
tip_share = ((percent_tip_to_share+bill)/number)
message = f"Each person should pay: ${round(tip_share, 2)}"
print(message)