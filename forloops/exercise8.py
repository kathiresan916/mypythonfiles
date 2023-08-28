#N numbers of Natural numbers & their Sum:

a=[]
for i in range (7):
    num=int(input("Enter your numbers:"+str(i+1)))
    a.append(num)
print(a)
sum=0
for i in a:
    sum=sum+i
print(sum)