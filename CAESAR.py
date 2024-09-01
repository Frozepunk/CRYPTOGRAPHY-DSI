def caesar_cipher(text, kv, mode='encrypt'):
    result = []
    if mode == 'decrypt':
        kv = -kv

    for char in text:
        if char.islower():
            base = ord('a')
            res = chr((ord(char) - base + kv) % 26 + base)
            result.append(res)
        elif char.isupper():
            base = ord('A')
            res = chr((ord(char) - base + kv) % 26 + base)
            result.append(res)
        elif char.isdigit():
            base = ord('0')
            res = chr((ord(char) - base + kv) % 10 + base)
            result.append(res)
        else:
            result.append(char)

    return ''.join(result)

text = input("Enter text: ")
kv = int(input("Shift value (kv): "))
mode = input("Choose mode ('encrypt' or 'decrypt'): ").strip().lower()

output = caesar_cipher(text, kv, mode)
print(output)
