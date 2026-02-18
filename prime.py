n=int(input("the number you want to see if it is prime or not"))
i=n-1
def prime(n,i):
    if n==1 and n==2:
        return "prime"
    elif n%i==0:
        return "not prime"
    if i>2:
        return prime(n,i-1)
    return "prime"

primes=prime(n,i)
print(primes)
