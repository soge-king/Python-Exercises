import re  # Import regex module for pattern matching
import secrets  # Import secrets for generating secure random numbers
import string  # Import string constants

# Define a function to generate a password
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define the possible characters for the password
    letters = string.ascii_letters  # Includes both uppercase and lowercase letters
    digits = string.digits  # Includes digits from 0-9
    symbols = string.punctuation  # Includes special characters like !, @, #

    # Combine all possible characters into a single string
    all_characters = letters + digits + symbols

    while True:
        password = ''  # Initialize password as an empty string
        # Generate a password of the specified length
        for _ in range(length):
            password += secrets.choice(all_characters)  # Securely pick a random character
        
        # Define constraints to ensure the password meets requirements
        constraints = [
            (nums, r'\d'),  # At least `nums` digits
            (special_chars, fr'[{symbols}]'),  # At least `special_chars` special characters
            (uppercase, r'[A-Z]'),  # At least `uppercase` uppercase letters
            (lowercase, r'[a-z]')  # At least `lowercase` lowercase letters
        ]

        # Check if all constraints are satisfied
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break  # Exit loop if all constraints are met
    
    return password  # Return the generated password

# This block executes only if the script is run directly (not imported as a module)
if __name__ == '__main__':    
    new_password = generate_password()  # Generate a new password using default parameters
    print('Generated password:', new_password)  # Output the generated password
