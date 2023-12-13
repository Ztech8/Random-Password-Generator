import random

def generate_password(length, all_chars):
    return "".join(random.sample(all_chars, length))

def save_passwords_to_file(passwords, filename):
    if not filename.lower().endswith('.txt'):
        filename += '.txt'
    
    try:
        with open(filename, 'w') as file:
            for password in passwords:
                file.write(password + '\n')
        print(f"Passwords saved to {filename}")
    except Exception as e:
        print(f"Error saving passwords: {e}")

def print_banner():
    banner = """
    
 /$$$$$$$  /$$$$$$$   /$$$$$$ 
| $$__  $$| $$__  $$ /$$__  $$
| $$  \ $$| $$  \ $$| $$  \__/
| $$$$$$$/| $$$$$$$/| $$ /$$$$
| $$__  $$| $$____/ | $$|_  $$
| $$  \ $$| $$      | $$  \ $$
| $$  | $$| $$      |  $$$$$$/
|__/  |__/|__/       \______/ 
                              
                              
                              
    """
    print(banner)

uppercase_letters = "ABCDEFGHIOPQLNVZXWJKLRTYU"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*_?-/+"

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

print_banner()

try:
    length = int(input("Enter the length of the password: "))
    amount = int(input("Enter how many passwords to create: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

passwords = []

for x in range(amount):
    password = generate_password(length, all_chars)
    passwords.append(password)
    print(password)

save_passwords_option = input("\nDo you want to save these passwords to a file? (yes/no): ").lower()
if save_passwords_option in ['y', 'yes']:
    filename = input("Enter the filename to save passwords (without extension): ")
    save_passwords_to_file(passwords, filename)
