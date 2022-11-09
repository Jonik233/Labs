import argparse
import operator

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("action", type=str, help="function")
    parser.add_argument("first_number", type=int, help="integer")
    parser.add_argument("second_number", type=int, help="integer")
    
    args = parser.parse_args()
    
    first_number = args.first_number
    second_number = args.second_number
    
    if args.action == "multiply":
        print(operator.mul(first_number, second_number))
        
    elif args.action == "divide":
        try:
            print(operator.truediv(first_number, second_number))
        except ZeroDivisionError:
            print("Zerro division error")
            
    elif args.action == "add":
        print(operator.add(first_number, second_number))
    else:
        print(operator.sub(first_number, second_number))

if __name__ == '__main__':
    main()

