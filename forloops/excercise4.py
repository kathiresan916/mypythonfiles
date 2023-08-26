count_3=0
count_5=0
for i in range(1,100):
    if(i%3==0):
        count_3=count_3+1
    if(i%5==0):
        count_5=count_5+1
print("Divided by 3 Values are:", count_3)
print("Divided by 5 Values are:", count_5)