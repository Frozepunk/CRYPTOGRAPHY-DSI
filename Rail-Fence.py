def rail_fence_encrypt(plaintext, key):
    fence = [[] for _ in range(key)]
    rail = 0
    var = 1

    for char in plaintext:
        fence[rail].append(char)
        rail += var
        if rail == key - 1 or rail == 0:
            var = -var

    print("Fence Structure during Encryption:")
    for i, row in enumerate(fence):
        print(f"Rail {i}: {''.join(row)}")

    encrypted_text = ''.join(''.join(row) for row in fence)
    return encrypted_text

plaintext = input("Enter the plaintext for Rail Fence Encryption: ")
key = int(input("Enter the key (number of rails): "))

encrypted = rail_fence_encrypt(plaintext, key)
print("Encrypted Text:", encrypted)
