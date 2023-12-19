def generate_multiplication_table(number, table_range):
    print(f"Multiplication Table for {number}:\n")
    for i in range(1, table_range + 1):
        result = number*i
        print(f"{number} * {i} = {result}")


if __name__ == "__main__":
    multiplication_number = int(
        input("Enter a number for the multiplication table: "))
    table_range = 10

    generate_multiplication_table(multiplication_number, table_range)
