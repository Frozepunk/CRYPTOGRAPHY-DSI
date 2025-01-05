def vigenere(text, key, decrypt=False):
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    shift = -1 if decrypt else 1
    return ''.join(
        chr((ord(t) + shift * (ord(k) - 65) - 65) % 26 + 65) if t.isalpha() else t
        for t, k in zip(text.upper(), key.upper())
    )

text = input("Enter text: ")
key = input("Enter key: ")

encrypted = vigenere(text, key)
print("Encrypted text:", encrypted)

decrypted = vigenere(encrypted, key, decrypt=True)
print("Decrypted text:", decrypted)
