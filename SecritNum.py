#Program name:SecritNum simulator program 

#The correct password

#storing the user guess
guess = 0 

#set the secret no.

secretNum = 5

#create a while loop


while secretNum !=guess :
    guess = input ("Enter a numbre between 0 and 5")
    tries += 1 # Add 1 to the numbre of tries 

    #Check if password is wrong 
    if attempt != password:
        print("Incorrect password! Try again.")

#Once loop ends, check why it ended
if attempt  == password:
    print("✅Access granted!") # if password corrcet 
else:
    print("🚫Too many attempts. Try later.") # if user ran out of tries
    