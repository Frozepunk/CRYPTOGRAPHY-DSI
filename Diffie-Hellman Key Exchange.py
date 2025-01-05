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
