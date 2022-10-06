import argparse

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("first_number", type=int, help="integer")
    parser.add_argument("operator", type=str, help="operator(*, /, -, +)")
    parser.add_argument("second_number", type=int, help="integer")
    
    args = parser.parse_args()
    
    first_number = args.first_number
    second_number = args.second_number
    operator = args.operator
    
    if operator == "*":
        print(multiply(first_number, second_number))
        
    elif operator == "/":
        try:
            print(divide(first_number, second_number))
        except ZeroDivisionError:
            print("Zerro division error")
            
    elif operator == "+":
        print(add(first_number, second_number))
    else:
        print(subtract(first_number, second_number))

def add(a, b):
    return (a + b)

def subtract(a, b):
    return (a - b)

def multiply(a, b):
    return (a * b)

def divide(a, b):
    return (a / b)
     
if __name__ == '__main__':
    main()