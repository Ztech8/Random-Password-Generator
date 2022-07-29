def banner():
    a = ''' 
 _                _             
| |              | |            
| |__   __ _  ___| | _____ _ __ 
| '_ \ / _` |/ __| |/ / _ \ '__|
| | | | (_| | (__|   <  __/ |   
|_| |_|\__,_|\___|_|\_\___|_|   developed by Zthech8 programmer

    '''

    print(a)
    print("_" * 80)
banner()

import random 

uppercaser = str(input("Enter your letters >> "))
digits_input = int(input("Enter your digits >> "))
symbols_input = int(input("Enter your symbols >> "))

uppercase_letters = uppercaser
lowercase_letters = uppercase_letters.lower()
digits = digits_input
symbols = symbols_input

upper, lower, nums, syms =True ,True, True, True

all = ""

if upper:
    all += uppercase_letters 
if lower: 
    all +=  lowercase_letters 
if nums: 
    all += digits 
if syms: 
    all += symbols 

print("")
print("")


length = int(input(("Enter the length of the password >> ")))
print("")
amount = int(input("Enter how many passwords to create >> "))

for x in range(amount):
    password = "".join(random.sample(all, length)) 
    print(password)

