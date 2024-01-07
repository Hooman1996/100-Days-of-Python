# Hello this is the Day 2 - Python project
# The code is used to calculate the share each person should pay using the total bill,tip percentage and number of people
########################################################################################################################

print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float("1." + input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

bill_plus_tip = total_bill * tip_percentage
each_people_share = round((bill_plus_tip / number_of_people), 2)

print(f"Each person should pay {each_people_share}$")

