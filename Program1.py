"""
Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
  Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
  Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string
 

"""
val1 = float(input("enter a numeric value"))
val2 = float(input("enter another numeric value"))
result = 0
operation = input("enter the operation which you want to perform + - * /")

if operation == "+":
    result= val1+val2
    print(result)
    
elif operation == "-":
    result = val1-val2
    print(result)
elif operation == "*":
    result = val1*val2
    print(result)
elif operation == "/":
    result = val1/val2
    print(result)
else:
    print("invalid operation")

    