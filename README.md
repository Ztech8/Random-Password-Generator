# Password Generator

## Description

This Python script generates random passwords based on user preferences for length and character sets. It also provides an option to save the generated passwords to a text file.

## Features

- Customizable password length.
- Inclusion/exclusion of uppercase letters, lowercase letters, digits, and symbols.
- Option to save generated passwords to a text file.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/password-generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd password-generator
   ```

3. Run the script:

   ```bash
   python password_generator.py
   ```

4. Follow the prompts to specify password length, amount, and whether to save passwords to a file.

## Configuration

- Modify the character sets and flags in the script to customize the types of characters included in generated passwords.

```python
# Character sets for password generation
uppercase_letters = "ABCDEFGHIOPQLNVZXWJKLRTYU"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*_?-/+"

# Flags to include/exclude character sets
upper, lower, nums, syms = True, True, True, True
```

## Example

```bash
$ python password_generator.py

Enter the length of the password: 12
Enter how many passwords to create: 5

Generated Passwords:
1. hG@6UfLbZ*oQ
2. DnE@9yA0+L6F
3. 5W7%gRmPfI8e
4. J3@iBpYzUo9N
5. x4G^vS7l6R@A

Do you want to save these passwords to a file? (yes/no): yes
Enter the filename to save passwords (without extension): my_passwords
Passwords saved to my_passwords.txt
```
