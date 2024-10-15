def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def char_to_num(char):
    return ord(char.upper()) - ord('A')

def num_to_char(num):
    return chr(num + ord('A'))

def encrypt(message, key):
    encrypted_message = []
    print(f"Encrypting '{message}' with key '{key}':")
    
    message_nums = [char_to_num(c) for c in message if c.isalpha()]
    key_nums = [char_to_num(k) for k in key]
    
    print(f"Message as numbers: {message_nums}")
    print(f"Key as numbers: {key_nums}")
    
    for i in range(len(message)):
        if message[i].isalpha():
            shift = (char_to_num(message[i]) + char_to_num(key[i])) % 26
            encrypted_char = num_to_char(shift)
            encrypted_message.append(encrypted_char)
            print(f"Step {i + 1}: '{message[i]}' + '{key[i]}' -> '{encrypted_char}' (Shift: {shift})")
        else:
            encrypted_message.append(message[i])
            print(f"Step {i + 1}: Non-alphabet character '{message[i]}' remains unchanged.")
    
    return "".join(encrypted_message)

def decrypt(encrypted_message, key):
    decrypted_message = []
    print(f"\nDecrypting '{encrypted_message}' with key '{key}':")
    
    encrypted_nums = [char_to_num(c) for c in encrypted_message if c.isalpha()]
    key_nums = [char_to_num(k) for k in key]
    
    print(f"Encrypted message as numbers: {encrypted_nums}")
    print(f"Key as numbers: {key_nums}")
    
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isalpha():
            shift = (char_to_num(encrypted_message[i]) - char_to_num(key[i]) + 26) % 26
            decrypted_char = num_to_char(shift)
            decrypted_message.append(decrypted_char)
            print(f"Step {i + 1}: '{encrypted_message[i]}' - '{key[i]}' -> '{decrypted_char}' (Shift: {shift})")
        else:
            decrypted_message.append(encrypted_message[i])
            print(f"Step {i + 1}: Non-alphabet character '{encrypted_message[i]}' remains unchanged.")
    
    return "".join(decrypted_message)

def main():
    message = input("Enter the message to encrypt: ")
    key = input("Enter the key: ")
    
    full_key = generate_key(message, key)
    
    encrypted_message = encrypt(message, full_key)
    
    decrypted_message = decrypt(encrypted_message, full_key)
    
    print(f"\nFinal Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
