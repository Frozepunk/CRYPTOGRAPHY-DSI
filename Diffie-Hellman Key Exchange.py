import random

def diffie_hellman(p, g):
    a = random.randint(1, p-1)  # Alice's private key
    b = random.randint(1, p-1)  # Bob's private key

    A = pow(g, a, p)  # Alice's public key
    B = pow(g, b, p)  # Bob's public key

    shared_secret_A = pow(B, a, p)  # Alice's shared secret
    shared_secret_B = pow(A, b, p)  # Bob's shared secret

    assert shared_secret_A == shared_secret_B, "Shared secrets are not equal!"
    
    return shared_secret_A

# Example usage
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a base (g): "))
shared_secret = diffie_hellman(p, g)
print("Shared Secret:", shared_secret)
