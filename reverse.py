n=int(input("number "))
temp=n
rev=0
def revers(temp,rev):
    if temp<1:
        return rev
    val=temp%10
    rev=rev*10+val
    temp=temp//10
    return revers(temp,rev)

good=revers(temp,rev)
print(good)

    