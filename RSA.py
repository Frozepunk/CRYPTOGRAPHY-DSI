import math
from sympy import mod_inverse
p = int(input("Enter the value of p (prime): "))
q = int(input("Enter the value of q (prime): "))
n = p * q
phi = (p - 1) * (q - 1)
print("n =", n)
print("phi(n) =", phi)
e = int(input("Enter the value of e (1 < e < phi(n)): "))
while e >= phi or math.gcd(e, phi) != 1:
    print("Invalid e. Ensure 1 < e < phi (n)")
    e = int(input("Enter a valid value for e: "))
print("e =", e)
d = mod_inverse(e, phi)
print("d =", d)
print(f'Public key: ({e}, {n})')
print(f'Private key: ({d}, {n})')
msg = int(input("Enter the value of the message (as an integer): "))
print(f'Original message: {msg}')
C = pow(msg, e, n)
print(f'Encrypted message: {C}')
M = pow(C, d, n)
print(f'Decrypted message: {M}')
