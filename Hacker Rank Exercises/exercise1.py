#Print the list of integers without using any string:

def print_numbers(n):
    for i in range (1, n+1):
        print(i,  end="")

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print_numbers(n)