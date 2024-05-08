print("Welcome to the tip calculator!")

bill_amount = float(input("What was the total bill? "))
tip_percent = float(input("What percent would you like to tip? (10, 15, 20) ")) / 100
amt_of_diners = int(input("How many people want to split the bill? "))

tip_amount = bill_amount * tip_percent

each_pays = (bill_amount + tip_amount) / amt_of_diners

print(f"Each person should pay: {round(each_pays, 2)}")
