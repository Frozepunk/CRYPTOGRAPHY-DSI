def vigenere_encrypt(plaintext, key):
    key = key.upper()
    key_sequence = []
    ciphertext = []
    alpha_numeric_plaintext = []
    alpha_numeric_key = []
    calculation_steps = []

    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            key_sequence.append(key[i % len(key)])
            alpha_numeric_key.append(str(shift))  # Key's alphabetic numeric value (0-25)
            if char.isupper():
                value = ord(char) - ord('A')
                alpha_numeric_plaintext.append(str(value))  # Plaintext numeric value (0-25)
                result = (value + shift) % 26 + ord('A')
                ciphertext.append(chr(result))
                calculation_steps.append(f"({value} + {shift}) % 26 = {chr(result)}")
            else:
                value = ord(char) - ord('a')
                alpha_numeric_plaintext.append(str(value))
                result = (value + shift) % 26 + ord('a')
                ciphertext.append(chr(result))
                calculation_steps.append(f"({value} + {shift}) % 26 = {chr(result)}")
        else:
            ciphertext.append(char)
            key_sequence.append(' ')
            alpha_numeric_plaintext.append(' ')
            alpha_numeric_key.append(' ')

    print("\n--- Vigenère Encryption Process ---")
    print("Key Sequence:        ", ''.join(key_sequence))
    print("Plaintext Alphabetic:", ' '.join(alpha_numeric_plaintext))
    print("Key Alphabetic:      ", ' '.join(alpha_numeric_key))
    print("Calculation Steps:   ", ' | '.join(calculation_steps))
    return ''.join(ciphertext)


def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    key_sequence = []
    plaintext = []
    alpha_numeric_ciphertext = []
    alpha_numeric_key = []
    calculation_steps = []

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            key_sequence.append(key[i % len(key)])
            alpha_numeric_key.append(str(shift))  # Key's alphabetic numeric value (0-25)
            if char.isupper():
                value = ord(char) - ord('A')
                alpha_numeric_ciphertext.append(str(value))  # Ciphertext numeric value (0-25)
                result = (value - shift) % 26 + ord('A')
                plaintext.append(chr(result))
                calculation_steps.append(f"({value} - {shift}) % 26 = {chr(result)}")
            else:
                value = ord(char) - ord('a')
                alpha_numeric_ciphertext.append(str(value))
                result = (value - shift) % 26 + ord('a')
                plaintext.append(chr(result))
                calculation_steps.append(f"({value} - {shift}) % 26 = {chr(result)}")
        else:
            plaintext.append(char)
            key_sequence.append(' ')
            alpha_numeric_ciphertext.append(' ')
            alpha_numeric_key.append(' ')

    print("\n--- Vigenère Decryption Process ---")
    print("Key Sequence:          ", ''.join(key_sequence))
    print("Ciphertext Alphabetic: ", ' '.join(alpha_numeric_ciphertext))
    print("Key Alphabetic:        ", ' '.join(alpha_numeric_key))
    print("Calculation Steps:     ", ' | '.join(calculation_steps))
    return ''.join(plaintext)


def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice. Please select 'E' or 'D'.")
        return
    
    text = input("Enter the text: ")
    key = input("Enter the key: ")

    if choice == 'E':
        encrypted = vigenere_encrypt(text, key)
        print("Encrypted Text:", encrypted)
    else:
        decrypted = vigenere_decrypt(text, key)
        print("Decrypted Text:", decrypted)


if __name__ == "__main__":
    main()
