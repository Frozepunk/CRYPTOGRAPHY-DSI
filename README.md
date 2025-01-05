# CRYPTOGRAPHY
### ceasar cpher

```
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

```

### RSA 

```
import math 
p=int(input("Enter the value of P:->"))
q=int(input("Enter the value of Q:->"))
n=p*q
phi_n=((p-1)*(q-1))
e=int(input("Enter the value of E:"))
while e<phi_n:
    if math.gcd(e,phi_n)==1:
        break
    e+=1
d=pow(e,-1,phi_n)
print(f"Public key ({e,n})")
print(f"Private key({d,n})")
m=int(input("Enter the value of M:"))
c=math.pow(m,e)%n
de=math.pow(c,d)%n
print(f"Encrypt{c}")
print(f"Decrypt {de}")

```

### Rail fence 
```
def rail_fence_cipher(text, key):
    rail = [''] * key
    idx, step = 0, 1
    for char in text:
        rail[idx] += char
        idx += step
        if idx == 0 or idx == key - 1:
            step *= -1
    return ''.join(rail)


text = input("Enter the text: ")
key = int(input("Enter the key: "))

encrypted = rail_fence_cipher(text, key)
print("Encrypted text:", encrypted)

print(rail_fence_cipher(text, key))
```

### Vignear cipher
```
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
```

### Playfair cipher 
```
import string

def generate_matrix(keyword):
    matrix = [[' ' for _ in range(5)] for _ in range(5)]
    keyword = keyword.upper()
    keyword_chars = []
    seen = set()
    
    for char in keyword:
        if char not in seen and char != 'J':
            keyword_chars.append(char)
            seen.add(char)
    
    random_chars = [char for char in string.ascii_uppercase if char not in keyword_chars and char != 'J']
    random_chars.sort()

    index = 0
    for i in range(5):
        for j in range(5):
            if index < len(keyword_chars):
                matrix[i][j] = keyword_chars[index]
                index += 1
            else:
                matrix[i][j] = random_chars.pop(0)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

def prepare_text(text):
    text = text.upper().replace(' ', '')
    result = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] != text[i + 1]:
            result.append(text[i:i + 2])
            i += 2
        else:
            result.append(text[i] + 'X')
            i += 1
    return result

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char or (char == 'I' and matrix[i][j] == 'J') or (char == 'J' and matrix[i][j] == 'I'):
                return (i, j)

def encrypt(matrix, text):
    result = []
    for pair in text:
        pos1 = find_position(matrix, pair[0])
        pos2 = find_position(matrix, pair[1])
        if pos1[0] == pos2[0]:  
            result.append(matrix[pos1[0]][(pos1[1] + 1) % 5] + matrix[pos2[0]][(pos2[1] + 1) % 5])
        elif pos1[1] == pos2[1]:  
            result.append(matrix[(pos1[0] + 1) % 5][pos1[1]] + matrix[(pos2[0] + 1) % 5][pos2[1]])
        else:  
            result.append(matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]])
    return ' '.join(result)

def decrypt(matrix, text, original_text):
    result = []
    original_text = original_text.upper().replace(' ', '')  # Remove spaces for comparison
    
    for idx, pair in enumerate(text.split()):
        pos1 = find_position(matrix, pair[0])
        pos2 = find_position(matrix, pair[1])
        
        if pos1[0] == pos2[0]:  
            decrypted_pair = matrix[pos1[0]][(pos1[1] - 1) % 5] + matrix[pos2[0]][(pos2[1] - 1) % 5]
        elif pos1[1] == pos2[1]:  
            decrypted_pair = matrix[(pos1[0] - 1) % 5][pos1[1]] + matrix[(pos2[0] - 1) % 5][pos2[1]]
        else:  
            decrypted_pair = matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
        
        # Check the original plain text for 'I' or 'J' and adjust the decrypted text accordingly
        for i in range(2):
            if original_text[idx * 2 + i] == 'I' and decrypted_pair[i] == 'J':
                decrypted_pair = decrypted_pair[:i] + 'I' + decrypted_pair[i + 1:]
            elif original_text[idx * 2 + i] == 'J' and decrypted_pair[i] == 'I':
                decrypted_pair = decrypted_pair[:i] + 'J' + decrypted_pair[i + 1:]
        
        result.append(decrypted_pair)
    
    return ''.join(result)

def main():
    text = input("Enter the plain text: ")
    keyword = input("Enter the keyword: ")
    matrix = generate_matrix(keyword)
    print("\nMatrix:")
    print_matrix(matrix)
    
    prepared_text = prepare_text(text)
    print("Prepared text:", ' '.join(prepared_text))
    
    encrypted_text = encrypt(matrix, prepared_text)
    print("\nEncrypted text:", encrypted_text)

    decrypted_text = decrypt(matrix, encrypted_text, text)  # Pass original text
    print("\nDecrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
```

### Diffie hellman key exchnage 
```
def power(base, exp, mod):
    if exp == 0:
        return 1
    half = power(base, exp // 2, mod)
    half = (half * half) % mod
    return half if exp % 2 == 0 else (half * base) % mod

def main():
    n = int(input("Enter the value of n (modulus): "))
    g = int(input("Enter the value of g (base): "))
    x = int(input("Enter the private key for the first person (x): "))
    a = power(g, x, n)
    print(f"Public key of the first person: {a}")
    y = int(input("Enter the private key for the second person (y): "))
    b = power(g, y, n)
    print(f"Public key of the second person: {b}")
    key1 = power(b, x, n)
    key2 = power(a, y, n)
    print(f"Shared key for the first person: {key1}")
    print(f"Shared key for the second person: {key2}")

if __name__ == "__main__":
    main()
````