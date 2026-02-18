def sums(*argws):
    return sum(argws)
num=sums(1,2,3,4,5)
print(num)

def sums(**kwargs):
    return sum(kwargs.values())
num=sums(a=1,b=2,c=3,d=4,e=5)
print(num)