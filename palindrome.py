num="ashutosh"
rev=""
for i in num:
    rev= i+rev
print(rev)

num="madam"
n=len(num)
left,right=0,n-1
flag=True
while left<right:
    if num[left]!=num[right]:
        flag=False
        break
    else:
        left+=1
        right-=1

print(flag)
