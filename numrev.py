#Program Description : The purpose of this program is to reverse the number entered by the user


#Take the number from the user as a string (so we can access each digit easily)
n = input("Enter a number:")

rev = ""                 #This will store the revesed number
i = len(n) - 1        # Start from  the last index of string 

#Loop backward through the string 
while i >= 0:
    rev = rev + n[i]   #Add the corrent character to the reversed string 
    i -= 1            #More to the previous character 

#Display the revesed result 
print(f"The numbre reversed is : {rev}")
