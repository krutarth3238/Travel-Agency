import string
from math import gcd

def additive_cipher_encrypt(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + key) % 26 + offset)
        else:
            result += char
    return result

def additive_cipher_decrypt(cipher, key):
    return additive_cipher_encrypt(cipher, -key)

def multiplicative_cipher_encrypt(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr(((ord(char) - offset) * key) % 26 + offset)
        else:
            result += char
    return result

def multiplicative_cipher_decrypt(cipher, key):
    inverse_key = pow(key, -1, 26)  # Find modular multiplicative inverse of key
    return multiplicative_cipher_encrypt(cipher, inverse_key)

def affine_cipher_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    result = ''
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr(((ord(char) - offset) * a + b) % 26 + offset)
        else:
            result += char
    return result

def affine_cipher_decrypt(cipher, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    a_inverse = pow(a, -1, 26)  # Modular multiplicative inverse of a
    result = ''
    for char in cipher:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((a_inverse * ((ord(char) - offset) - b)) % 26 + offset)
        else:
            result += char
    return result

def main():
    while True:
        print("\nChoose a cipher:")
        print("1. Additive Cipher")
        print("2. Multiplicative Cipher")
        print("3. Affine Cipher")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter text: ")
            key = int(input("Enter key: "))
            mode = input("Encrypt or Decrypt? (e/d): ").lower()
            if mode == 'e':
                print("Encrypted Text:", additive_cipher_encrypt(text, key))
            elif mode == 'd':
                print("Decrypted Text:", additive_cipher_decrypt(text, key))

        elif choice == '2':
            text = input("Enter text: ")
            key = int(input("Enter key: "))
            mode = input("Encrypt or Decrypt? (e/d): ").lower()
            if gcd(key, 26) != 1:
                print("Key must be coprime with 26.")
                continue
            if mode == 'e':
                print("Encrypted Text:", multiplicative_cipher_encrypt(text, key))
            elif mode == 'd':
                print("Decrypted Text:", multiplicative_cipher_decrypt(text, key))

        elif choice == '3':
            text = input("Enter text: ")
            a = int(input("Enter key 'a': "))
            b = int(input("Enter key 'b': "))
            mode = input("Encrypt or Decrypt? (e/d): ").lower()
            if mode == 'e':
                try:
                    print("Encrypted Text:", affine_cipher_encrypt(text, a, b))
                except ValueError as e:
                    print(e)
            elif mode == 'd':
                try:
                    print("Decrypted Text:", affine_cipher_decrypt(text, a, b))
                except ValueError as e:
                    print(e)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()