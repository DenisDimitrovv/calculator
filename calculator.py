def add(num, num2):
    return num + num2

def sub(num, num2):
    return num - num2

def multiply(num, num2):
    return num * num2

def divide(num, num2):
    return num / num2


while True:
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = input("Enter choice(1/2/3/4): ")
        if choice not in ('1', '2', '3', '4'):
            raise ValueError("Invalid choice. Please enter a number between 1 and 4.")

        num = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError as e:
        print("Invalid input:", e)
        continue

    if choice == '1':
        print(num, "+", num2, "=", add(num, num2))

    elif choice == '2':
        print(num, "-", num2, "=", sub(num, num2))

    elif choice == '3':
        print(num, "*", num2, "=", multiply(num, num2))

    elif choice == '4':
        print(num, "/", num2, "=", divide(num, num2))

    while True:
        next_calculation = input("Let's do another calculation? (yes/no): ")
        if next_calculation.lower() in ('yes', 'no'):
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            continue

    if next_calculation.lower() == "no":
        print("Exiting.")
        break
