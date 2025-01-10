#to print sum of even numbers

def sum_of_even_numbers(n):
    return sum(i for i in range(2, n + 1, 2))
try:
    n = int(input("Enter a positive integer: "))
    if n < 1:
        print("enter a positive integer greater than or equal to 1.")
    else:
        result = sum_of_even_numbers(n)
        print(f"sum of all even numbers between 1 and {n} is: {result}")
except ValueError:
    print("Invalid input! Please enter a valid positive integer.")
