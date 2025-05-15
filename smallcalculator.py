print("welcome to simple calculator")

#ask for operation
print("choose operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. divide (/)")

operation = input("Enter operation (+, -, *, /): ")
#get two numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# perform calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
     result = num1 / num2 
    else:
        result = 'Error! Division By zero.'
else:
     result = "Invalid operation"

# show result 
print("Result:", result)