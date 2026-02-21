def sums(*argws):
    return sum(argws)
result=sums(1,2,3,4,4)
print(result)

def rre(**kwargs):
    return sum(kwargs.values())

result=rre(a=1,b=2,c=3,d=4,e=5)
print(result)