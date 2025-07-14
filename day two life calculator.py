age = input("What is your current age?")
age_in_ds = int(age)*365
age_in_wks = int(age)*52
age_in_mths = int(age)*12
# sp baisically you find for the number of days , weeks and months if you were to live to 90 it would be, then you go ahead
# to relate that by subtracting your current age in days, weeks and months from that which you had for 90yrs, if you were to live
# to a 90 years to get the number of days, weeks and months left for you.
age_in_days  = 32850-age_in_ds
age_in_weeks = 4680-age_in_wks
age_in_months= 1080-age_in_mths
print(f"You have {age_in_days} days, {age_in_weeks} weeks, and {age_in_months} months left. ")
            
            
            
        