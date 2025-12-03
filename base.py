x = int (input("enter the first number : "))
y = int (input("enter the second number : "))
operation =  input ("enter the operation you want  to perform (+,-,*,/) : ")
if operation == '+':
    result =  x  +y
    print("the addtion of two number is : ", result)
elif operation == '-':
    result = x - y 
    print("the substraction of two nubwe is : ", result )

elif operation  == '*':
    result = x * y
    print ("the multipication of the two number is:", result)
elif operation == '/':
    if y != 0:
        result = x/y
        print("the division of two number is : ", result)
    else :
        print ("error: divisibel by zero is not allowed")
else:
    print("invlaid operation")
   