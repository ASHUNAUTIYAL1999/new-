num=[1,2,0,4,0,5,0,6]
n=len(num)
count,i=0,0
while i<n:
    if num[i]!=0:
        num[count],num[i]=num[i],num[count]
        count+=1
        i+=1
    else:
        i+=1
print(num)
