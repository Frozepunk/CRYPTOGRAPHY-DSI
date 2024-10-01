def vigenere_encrypt(plaintext, key):
    key = key.upper()
    ciphertext = []
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            if char.isupper():
                ciphertext.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            else:
                ciphertext.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    plaintext = []
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            if char.isupper():
                plaintext.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            else:
                plaintext.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
        else:
            plaintext.append(char)
    return ''.join(plaintext)

# Example usage
plaintext = input("Enter the plaintext for Vigenere: ")
key = input("Enter the key: ")
encrypted = vigenere_encrypt(plaintext, key)
print("Encrypted Text:", encrypted)
decrypted = vigenere_decrypt(encrypted, key)
print("Decrypted Text:", decrypted)
