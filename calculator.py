def calculator(num1,operation,num2):
    if operation == '+':
        result = num1+num2
    elif operation == '-':
        result = num1-num2    
    elif operation == '*':
        result = num1*num2    
    elif operation == '/':
        result = num1/num2    
    elif operation == '^':
        result = num1**num2
    return result

num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))
result = calculator(num1,operation,num2)
print('Result = ',result)