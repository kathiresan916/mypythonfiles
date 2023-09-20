#Pass / #Break / #Continue uses:

hi = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]

for you in hi:
    pass
    if (you ==0):
        current = you
        break
    elif(you%2 ==0):
        continue
    print(you)
print(current)