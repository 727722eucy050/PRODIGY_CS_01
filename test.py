def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            elif char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (E/D): ").strip().upper()
        if choice not in ['E', 'D']:
            print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")
            continue
        
        message = input("Enter your message: ").strip()
        shift = int(input("Enter the shift value: ").strip())
        
        if choice == 'E':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'D':
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        
        another = input("Do you want to perform another operation? (Y/N): ").strip().upper()
        if another != 'Y':
            break

if __name__ == "__main__":
    main()
