def banner():
    a = ''' 
 _                _             
| |              | |            
| |__   __ _  ___| | _____ _ __ 
| '_ \ / _` |/ __| |/ / _ \ '__|
| | | | (_| | (__|   <  __/ |   
|_| |_|\__,_|\___|_|\_\___|_|   developed by X4_X4 programmer

    '''

    print(a)
    print("_" * 80)
banner()

import random 


uppercase_letters = "ABCDEFGHİJKLMNQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789" 
symbols = ".-_*/@" 

upper, lower, nums, syms = True, True, True, True

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


length = int(input(("Enter how many characters you want: ")))
print("")
amount = int(input("Enter how many passwords to create: "))

for x in range(amount):
    password = "".join(random.sample(all, length)) 
    print(password)


    