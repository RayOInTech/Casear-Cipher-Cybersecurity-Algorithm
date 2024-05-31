#Ray_O_In-Tech Solo Casear Cipher Advanced Project 1 

# To execute this program, enter caesar_cipher.py in the terminal.
# This helps decrypt given input and therfore changing it to output with the ciphertext.

#Ray_O_In-Tech Solo Advanced Casear Cipher Project 1

# To execute this program, enter caesar_algorithm_advanced.py in the terminal.
# This helps decrypt given input and therfore changing it to output with the ciphertext.

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters are added as is
    
    return result

def main():
    import sys

    while True:
        print("\nCaesar Cipher Tool")
        print("==================")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        while True:
            choice = input("Choose an option (1/2/3): ")
            if choice in ['1', '2', '3']:
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        
        if choice == '3':
            print("Exiting...")
            sys.exit()

        text = input("Enter the text: ")
        while True:
            try:
                shift = int(input("Enter the shift value (0-25): "))
                if 0 <= shift <= 25:
                    break
                else:
                    print("Shift value must be between 0 and 25.")
            except ValueError:
                print("Invalid input. Please enter a valid integer between 0 and 25.")
        
        mode = 'encrypt' if choice == '1' else 'decrypt'
        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
