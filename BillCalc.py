#program Description Calculates bill 

#Asking user for Bill amt 

bill = float (input("Enter BILL amt "))  

#Asking user for no. of people 

People = int(input("Entre no. of people sharing the bill:"))

#Define tax and tip rates

tax_rate = 0.0825 
tip_rate = 0.15

#formula to caluculate   tax, tip and total 
tax=bill * tax_rate 

tip = bill * tip_rate 

total = bill + tax + tip 

#Calucalate amt each person owes 
per_person = total / People 

#Printing everything 

print("Rarestarant Bill Caluculator") 
print("----------------------------")
print(f" Original Bill {bill}")
print(f" Sales Tax: {tax}")
print(f"Tip 15% {tip}")
print(f"Here is the total bill{total}")
print(f"Each person's share   {per_person}") # 📝 Restaurant Bill Splitter
# This program calculates the total bill with tax & tip,
# then splits the cost among a group of friends.

# Step 1: Ask the user for the bill amount
bill = float(input("Enter the total bill amount: $"))

# Step 2: Ask how many people are splitting the bill
people = int(input("How many people are sharing the bill? "))

# Step 3: Define tax and tip rates
tax_rate = 0.0825   # 8.25% sales tax
tip_rate = 0.15     # 15% tip

# Step 4: Calculate tax, tip, and total
tax = bill * tax_rate
tip = bill * tip_rate
total = bill + tax + tip

# Step 5: Calculate how much each person pays
per_person = total / people

# Step 6: Print results with clear formatting
print("\n💵 Restaurant Bill Splitter 💵")
print("-----------------------------")
print(f"Original Bill: ${bill:.2f}")
print(f"Sales Tax (8.25%): ${tax:.2f}")
print(f"Tip (15%): ${tip:.2f}")
print(f"Total Bill: ${total:.2f}")
print(f"Each Person Pays: ${per_person:.2f}")
print("-----------------------------")





