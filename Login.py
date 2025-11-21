#Program name: Login Simulator Program
#Program Description: This program siulates a login system.
#The user must enter the correct password within three tries, or they're locked out

# The correct password
password = "python123"
#variable to store user input 
attempt = ""

#Track the number of tries
tries =0 

#Loop continues while     the password is wrong AND user has tries left 
while attempt != password and tries < 3:
    attempt = input ("Enter the password: ") # Ask user to type the password 
    tries += 1 # Add 1 to the number of tries 

     # Check if password is wrong 
    if attempt !=  password:
        print("Incorrect password! Try again.") 

#Once loop ends, check why it ended 
if attempt == password: 
    print("✅Access granted!")  # If password is correct 
else :
    print("🚫 Too many attempts. Try later.") #  If user ran out of tries 
    