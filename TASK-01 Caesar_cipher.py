
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
            result += shifted_char
        else:
            result += char

    return result

def main():
    print("Caesar Cipher Program")
    action = input("Would you like to (e)ncrypt or (d)ecrypt? ").lower()
    
    if action not in ['e', 'd']:
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")
        return

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if action == 'e':
        encrypted_message = caesar_cipher(message, shift, mode='encrypt')
        print(f"Encrypted message: {encrypted_message}")
    else:
        decrypted_message = caesar_cipher(message, shift, mode='decrypt')
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()

