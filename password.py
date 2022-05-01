#this is my cyber security project this is first important tool in cyber security

#code program started let we go 
import random 

#here we put the letters and numbers we need in the password 
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

#here we put how many characters to create a password
length = 10
#we put how many passwords to create
amount = 10000

for x in range(amount):
    password = "".join(random.sample(all, length)) 
    print(password)

#code program ended
