import random
from Crypto.Util.number import getPrime, inverse

def generate_rsa_keys(key_size=1024):
    e = 65537  # Public exponent
    p = getPrime(key_size // 2)
    q = getPrime(key_size // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    return ((e, n), (d, n))

def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    plaintext_int = [pow(ord(char), e, n) for char in plaintext]
    return plaintext_int

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_chars = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted_chars)

# Example usage
public_key, private_key = generate_rsa_keys(512)
plaintext = input("Enter the plaintext for RSA: ")
encrypted = rsa_encrypt(plaintext, public_key)
print("Encrypted Text:", encrypted)
decrypted = rsa_decrypt(encrypted, private_key)
print("Decrypted Text:", decrypted)
