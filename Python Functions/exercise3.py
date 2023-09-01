#Find Pass or Fail using Fuctions:

def pass_fail(a):
    if a>=35:
        return "Your're Pass"
    else:
        return "You're Fail"
    
a=int(input("Enter your Score:"))
result=pass_fail(a)
print (result)