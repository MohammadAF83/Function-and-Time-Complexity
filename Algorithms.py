def factorial(n):
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def find_max(numbers):
  
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def linear_search(numbers, target):
    
    for num in numbers:
        if num == target:
            return True
    return False


def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def login():
   
    username = "admin"
    password = "1234"

    print("=== Login ===")
    user = input("Username: ")
    pw = input("Password: ")

    if user == username and pw == password:
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials.\n")
        return False


def main():
    logged_in = False

    while True:
        print("Choose an option:")
        print("1. Factorial")
        print("2. Find Max")
        print("3. Linear Search")
        print("4. Fibonacci")
        print("5. Login")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "5":
            logged_in = login()

        elif choice == "6":
            print("Goodbye!")
            break

        elif not logged_in:
            print("Please login first!\n")

        elif choice == "1":
            n = int(input("Enter a number: "))
            print("Factorial =", factorial(n))
            print()

        elif choice == "2":
            numbers = input("Enter numbers separated by space: ").split()
            numbers = [int(x) for x in numbers]
            print("Max =", find_max(numbers))
            print()

        elif choice == "3":
            numbers = input("Enter numbers separated by space: ").split()
            numbers = [int(x) for x in numbers]
            target = int(input("Enter number to search for: "))
            print("Found?" , linear_search(numbers, target))
            print()

        elif choice == "4":
            n = int(input("Enter n: "))
            print("Fibonacci (iterative) =", fibonacci_iterative(n))
            print("Fibonacci (recursive) =", fibonacci_recursive(n))
            print()

        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()