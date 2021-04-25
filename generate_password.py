import random
letters = ['a','b','c','e','t','s','x','p','w','g','v','n']
symbols = ['!','@','#','%','*','+','^','&']
numbers = ['1','2','3','4','5','6','7','8','9']

print(" Welcome to generate Passwords : ")

nr_letters = int (input (" How many letters do you like in your password ? \n "))
nr_symbols = int (input (f" How many symbols do you like in your password ? \n "))
nr_numbers = int (input (f" How many numbers do you like in your password ? \n "))

#easy level
password =""
#nr_letters = 4
for char in range (1, nr_letters + 1) :
    password += random.choice(letters)
       
for char in range (1, nr_symbols + 1) :
    password += random.choice(symbols)

for char in range (1, nr_numbers + 1) :
    password += random.choice(numbers)   

print(password)    
        