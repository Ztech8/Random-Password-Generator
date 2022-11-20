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
print("")



uppercase_letters = ["ABCDEFGHIOPQLNVZXWJKLRTYU"]
lowercase_letters = uppercase_letters.lower()
digits = (1,2,3,4,5,6,7,8,9)
symbols = ("!@#$%^&*_?/")

upper, lower, nums, syms =True ,True, True, True

all = ""

if upper == str:
    all += uppercase_letters 
if lower == str: 
    all +=  lowercase_letters 
if nums: 
    all += digits 
if syms == str: 
    all += symbols 

print("")
print("")


length = int(input(("Enter the length of the password >> ")))
print("")
amount = int(input("Enter how many passwords to create >> "))

for x in range(amount):
    password = "".join(random.sample(all, length)) 
    print(password)

