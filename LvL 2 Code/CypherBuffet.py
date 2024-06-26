
def caesar(message, shift):
    """
    Encrypts or decrypts a message using the Caesar cipher.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char in alphabet:
            index = alphabet.find(char)
            new_index = (index + shift) % 26
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char
    return encrypted_text

def vigenere(message, key, vshift, encrypt=True):
    """
    Encrypts or decrypts a message using the Vigenere cipher, incorporating an additional shift (vshift).
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    key_index = 0

    for char in message.lower():
        if char in alphabet:
            index = alphabet.find(char)
            base_offset = alphabet.find(key[key_index % len(key)].lower())
            # Adjusting offset with vshift
            if encrypt:
                offset = (base_offset + vshift) % 26
                new_index = (index + offset) % 26
            else:
                offset = (base_offset - vshift) % 26
                new_index = (index - offset) % 26
            result += alphabet[new_index]
            key_index += 1
        else:
            result += char
    return result

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def to_morse_code(message, encryption=True):
    
    morse_code = ''
    for char in message.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
    return morse_code

def from_morse_code(morse_code, encryption=True):
        
    message = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for char, morse in morse_dict.items():
            if morse == code:
                message += char
    return message


def bacon_cipher(message, encrypt=True):
    # Implement Bacon cipher encryption/decryption
    return "Bacon Cipher Placeholder"
def main():
    while True:
        try:
            yerfn = input('What is your first name? ')
            yerln = input('What is your last name? ')

            if not (yerfn.isalpha() and yerln.isalpha()):
                raise ValueError("Name must contain only alphabetic characters")

            initial2 = yerln[0].upper()
            print(f'Hello {yerfn} {initial2}, before we begin...')
            break
        except ValueError as e:
            print("Error: ", e)
    
    while True:
        try:
            print("Select the cipher method:\nA: Caesar Cipher\nB: Vigenere Cipher\nC: Bacon Cipher\nD: Morse Code")
            choice = input("Your choice (A/B/C/D): ").upper()
        
            if choice not in ['A', 'B', 'C', 'D']:
                raise ValueError("Invalid choice")
            break
        except ValueError as e:
            print("Error: ", e)

    if choice != 'D':
        text = input("Enter the text to encrypt/decrypt: ")

    result = None
    if choice == 'A':
        shift = int(input("Enter the shift for the Caesar cipher: "))
        result = caesar(text, shift)
    elif choice == 'B':
        key = input("Enter the key for the Vigenere cipher: ").lower()
        vshift = int(input("Enter cipher shift: "))
        result = vigenere(text, key, vshift, encrypt=True)  # Assuming encryption by default
    elif choice == 'C':
        result = bacon_cipher(text)
    elif choice == 'D':
        morsechoice = input("Choose an option:\n1: Text to Morse code\n2: Morse code to text\n-1: Quit\n")
        if morsechoice == '1':
            message = input("Enter a message to convert to Morse code: ")
            result = to_morse_code(message)
        elif morsechoice == '2':
            morse_code = input("Enter a Morse code sequence to convert to text: ")
            result = from_morse_code(morse_code)
        else:
            print("Quitted successfully")
            return

    if result is not None:
        print("Result:", result)


if __name__ == "__main__":
    main()
