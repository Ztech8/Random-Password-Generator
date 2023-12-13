
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



import random 

print("")

uppercase_letters = "ABCDEFGHIOPQLNVZXWJKLRTYU"
lowercase_letters = uppercase_letters.lower()
digits = "123456789"
symbols = "!@#$%^&*_?/"

upper, lower, nums, syms = True, True, True, True

all_chars = ""

if upper:
    all_chars += uppercase_letters
if lower:
    all_chars += lowercase_letters
if nums:
    all_chars += digits
if syms:
    all_chars += symbols

print("")
print("")

length = int(input("Enter the length of the password >> "))
print("")
amount = int(input("Enter how many passwords to create >> "))

for x in range(amount):
    password = "".join(random.sample(all_chars, length))
    print(password)
