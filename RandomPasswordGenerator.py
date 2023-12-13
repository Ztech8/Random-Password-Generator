def banner():
    a = '''
       
 /$$$$$$$  /$$$$$$$   /$$$$$$ 
| $$__  $$| $$__  $$ /$$__  $$
| $$  \ $$| $$  \ $$| $$  \__/
| $$$$$$$/| $$$$$$$/| $$ /$$$$
| $$__  $$| $$____/ | $$|_  $$
| $$  \ $$| $$      | $$  \ $$
| $$  | $$| $$      |  $$$$$$/
|__/  |__/|__/       \______/ 
                              
                                 developed by Sumerian Code

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

