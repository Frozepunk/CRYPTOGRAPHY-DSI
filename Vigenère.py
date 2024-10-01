def vigenere_encrypt(plaintext, key):
    key = key.upper()  # Ensure the key is in uppercase
    key_sequence = []  # To store the key sequence for display
    ciphertext = []    # To store the encrypted text
    
    for i, char in enumerate(plaintext):
        if char.isalpha():  # Encrypt only alphabetic characters
            shift = ord(key[i % len(key)]) - ord('A')  # Calculate shift based on the key character
            key_sequence.append(key[i % len(key)])     # Append corresponding key character for display
            if char.isupper():
                # Encrypt uppercase letters
                ciphertext.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            else:
                # Encrypt lowercase letters
                ciphertext.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            # If the character is not a letter, append it unchanged
            ciphertext.append(char)
            key_sequence.append(' ')  # Append a space to keep the key sequence aligned
    
    print("Key Sequence:  ", ''.join(key_sequence))  # Display the key sequence
    print("Plaintext:     ", plaintext)              # Display the original plaintext
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    key = key.upper()  # Ensure the key is in uppercase
    key_sequence = []  # To store the key sequence for display
    plaintext = []     # To store the decrypted text
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():  # Decrypt only alphabetic characters
            shift = ord(key[i % len(key)]) - ord('A')  # Calculate shift based on the key character
            key_sequence.append(key[i % len(key)])     # Append corresponding key character for display
            if char.isupper():
                # Decrypt uppercase letters
                plaintext.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            else:
                # Decrypt lowercase letters
                plaintext.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
        else:
            # If the character is not a letter, append it unchanged
            plaintext.append(char)
            key_sequence.append(' ')  # Append a space to keep the key sequence aligned
    
    print("Key Sequence:  ", ''.join(key_sequence))  # Display the key sequence
    print("Ciphertext:    ", ciphertext)             # Display the original ciphertext
    return ''.join(plaintext)

# Example usage
plaintext = input("Enter the plaintext for Vigenere: ")
key = input("Enter the key: ")
encrypted = vigenere_encrypt(plaintext, key)
print("Encrypted Text:", encrypted)
decrypted = vigenere_decrypt(encrypted, key)
print("Decrypted Text:", decrypted)
