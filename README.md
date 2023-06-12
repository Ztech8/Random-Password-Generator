# Random Password Generator

This Python script generates random passwords based on the specified criteria such as the length of the password and the types of characters to include.

## Usage

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.

### Running the Script

1. Run the script by executing the following command:

   ```bash
   python random_password_generator.py
   ```

2. Follow the prompts on the terminal to specify the password criteria:
   - Enter the length of the password.
   - Enter how many passwords to generate.

3. Once you provide the necessary inputs, the script will generate the requested number of random passwords based on the specified criteria.

## How It Works

The script first defines a function called `banner()` that prints a banner with the developer's name.

Next, the script imports the `random` module, which is used for generating random passwords.

The script allows you to customize the criteria for generating passwords. You can enable or disable the inclusion of uppercase letters, lowercase letters, numbers, and symbols in the generated passwords by setting the corresponding variables (`upper`, `lower`, `nums`, `syms`) to `True` or `False`.

The script then creates a variable `all` to store the characters based on the enabled criteria. It concatenates the respective character sets based on the enabled criteria.

The script prompts the user to enter the desired length of the password and the number of passwords to generate.

Using a loop, the script generates random passwords by selecting characters from the `all` variable using the `random.sample()` function. The selected characters are joined together to form a password.

The generated passwords are then printed to the terminal.

## Customization

You can modify the code to suit your specific needs:

- Adjust the character sets (e.g., `uppercase_letters`, `lowercase_letters`, `digits`, `symbols`) to include or exclude specific characters.
- Modify the prompts or add validation for the user inputs.
- Customize the output format of the generated passwords.

Feel free to modify and integrate this code into your own projects as needed.
