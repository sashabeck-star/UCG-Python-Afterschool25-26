


#varible to store user name 
name = input("Enter your name: ")

#While loop will run as long as the varible name has nothing stored in it 
while name == "" or not name.isalpha():
  print("You did not enter your name")
  #Asking the user to enter their name in case they didn't type anything 
  name = input("Enter your name:")

#Exit out of the loop once the user has typed their 
print(f"Hello {name}")
 
