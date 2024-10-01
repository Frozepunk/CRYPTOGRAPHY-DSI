def rail_fence_encrypt(plaintext, key):
    fence = [[] for _ in range(key)]
    rail = 0
    var = 1

    for char in plaintext:
        fence[rail].append(char)
        rail += var
        if rail == key - 1 or rail == 0:
            var = -var
    
    encrypted_text = ''.join(''.join(row) for row in fence)
    return encrypted_text

def rail_fence_decrypt(ciphertext, key):
    fence = [[] for _ in range(key)]
    rail_len = [0] * key
    rail = 0
    var = 1

    for i in range(len(ciphertext)):
        rail_len[rail] += 1
        rail += var
        if rail == key - 1 or rail == 0:
            var = -var

    idx = 0
    for r in range(key):
        for i in range(rail_len[r]):
            fence[r].append(ciphertext[idx])
            idx += 1

    rail = 0
    var = 1
    result = []
    for i in range(len(ciphertext)):
        result.append(fence[rail].pop(0))
        rail += var
        if rail == key - 1 or rail == 0:
            var = -var

    return ''.join(result)

# Example usage
plaintext = input("Enter the plaintext for Rail Fence: ")
key = int(input("Enter the key: "))
encrypted = rail_fence_encrypt(plaintext, key)
print("Encrypted Text:", encrypted)
decrypted = rail_fence_decrypt(encrypted, key)
print("Decrypted Text:", decrypted)
