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
