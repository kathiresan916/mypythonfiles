a=input("Enter a Character:").lower()
if a .isalpha() and len(a)==1:
    if a in 'aeiou':
        print("Entered Character is Vowel")
    else:
        print("Entered Character is Consonet")
else:
    print("Please enter single Alphanumberic Character")
