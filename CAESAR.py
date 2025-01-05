def caesar_cipher():
    text = input("Enter text: ")
    key = int(input("Enter the key value: "))

    def shift(char, key, base, range_size):
        return chr((ord(char) - base + key) % range_size + base)

    # Encryption
    encrypted = ''.join(
        shift(char, key, ord('a'), 26) if char.islower() else
        shift(char, key, ord('A'), 26) if char.isupper() else
        shift(char, key, ord('0'), 10) if char.isdigit() else
        char
        for char in text
    )
    print("Encrypted text-->", encrypted)

    # Decryption
    decrypted = ''.join(
        shift(char, -key, ord('a'), 26) if char.islower() else
        shift(char, -key, ord('A'), 26) if char.isupper() else
        shift(char, -key, ord('0'), 10) if char.isdigit() else
        char
        for char in encrypted
    )
    print("Decrypted text-->", decrypted)

caesar_cipher()
