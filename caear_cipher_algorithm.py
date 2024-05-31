#Ray_O_In-Tech Solo Casear Cipher Project 1

# To execute this program, enter caesar_cipher.py in the terminal.
# This helps decrypt given input and therfore changing it to output with the ciphertext.

def caesar_cipher_encrypt(text, shift):
    result = ""
    
    # For moving through each character in the text
    for char in text:
        # This encrypts the uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # This encrypts the lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char   
    
    return result




def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

# Testing Area
if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    shift = int(input("Enter shift value: "))
    ciphertext = caesar_cipher_encrypt(plaintext, shift)
    decrypted_text = caesar_cipher_decrypt(ciphertext, shift)

    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted text: {decrypted_text}")
