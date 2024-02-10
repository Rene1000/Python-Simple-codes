#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

sletters=""
ssymbols=""
snumbers=""
for i in range (0,nr_letters):
  rn=random.randint(0,len(letters)-1)
  sletters+=letters[rn]
for i in range (0,nr_symbols):
  rn=random.randint(0,len(symbols)-1)
  ssymbols+=symbols[rn]
for i in range (0,nr_numbers):
  rn=random.randint(0,len(numbers)-1)
  snumbers+=numbers[rn]
  
passwordprototype=sletters+ssymbols+snumbers

print(passwordprototype)

#ahora convertiremos el string en una lista haciendo un  casting
passwordprototype=list(passwordprototype)


#ahora reborujaremos esa lista con la funcion shuffle
random.shuffle(passwordprototype)
finalpassword=""
for i in range(0,len(passwordprototype)):
  finalpassword+=passwordprototype[i]

print("\nYour secure password is: "+""+'"'+finalpassword+'"')