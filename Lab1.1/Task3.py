import argparse

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("expression", type=str)
    
    expression = parser.parse_args().expression
    
    if any(ch.isalpha() or ch.isspace() for ch in expression):
        print((False, None))
    else:
        result = 0
        digits = []
        operations = []
        
        for i in range(len(expression)):
            
            if expression[i].isdigit():
                j = i
                number = ""
                while j < len(expression) and expression[j].isdigit():
                    number += expression[j]
                    j += 1
                digits.append(number)
                if j == len(expression): 
                    break
                
            else:   
                if not expression[i + 1].isdigit():
                    print((False, None))
                else:
                    operations.append(expression[i])
        
        if len(operations) == 0:
            print((True, *digits[:]))
            
        else:
            operation = 0
            digit = 1
            result += int(digits[0])
            while(digit < len(digits)):
                if operations[operation] == "+":
                    result += int(digits[digit])
                else:
                    result -= int(digits[digit])
                operation += 1
                digit += 1
            print((True, result))
                
if __name__ == '__main__':
    main()
