#Guessing game:

number = 5

count = 0
limit = 3

while count < limit:
    guess = int(input("Guess the Number: "))
    count += 1
    if guess == number:
        print("You won..!")
        break
else:
    print("You loose..!")