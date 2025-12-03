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
print(f"Each person's share   {per_person}") 





