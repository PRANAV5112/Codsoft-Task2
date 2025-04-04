def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error! Division by zero."

def power(x, y):
    return x ** y

def calculator():
    print("\nSimple Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (**)")
    
    while True:
        choice = input("\nEnter choice (1/2/3/4/5) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting... Goodbye!")
            break
        
        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                operations = {
                    '1': add,
                    '2': subtract,
                    '3': multiply,
                    '4': divide,
                    '5': power
                }

                result = operations[choice](num1, num2)
                print(f"Result: {result}")

            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    calculator()
