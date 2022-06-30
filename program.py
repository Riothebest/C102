print("Hey, this is your calculator")
calculation = input("What operation would you like to use (Enter +,-,*,/): ")

def add():
    first_no_I = input("What is the first number: ")
    second_no_I = input("What is your second number: ")
    third_no_I = "0"
    yes_or_no = input("Is there a 3rd number(Y or N): ")
    if yes_or_no == "Y":
        third_no_I = input("Enter 3rd number: ")
    first_no = int(first_no_I)
    second_no = int(second_no_I)
    third_no=  int(third_no_I)
    sum = first_no+second_no+third_no
    sum1 = str(sum)
    print("The sum is: "+sum1)

def substraction():
    first_no_I = input("What is the first number: ")
    second_no_I = input("What is your second number: ")
    first_no = int(first_no_I)
    second_no = int(second_no_I)
    sub = first_no-second_no
    sub1 = str(sub)
    print("The sum is: "+sub1)

def multiply():
    first_no_I = input("What is the first number: ")
    second_no_I = input("What is your second number: ")
    first_no = int(first_no_I)
    second_no = int(second_no_I)
    product = first_no*second_no
    product1 = str(product)
    print("The sum is: "+product1)

def divide():
    first_no_I = input("What is the first number: ")
    second_no_I = input("What is your second number: ")
    first_no = int(first_no_I)
    second_no = int(second_no_I)
    product = first_no/second_no
    product1 = str(product)
    print("The sum is: "+product1)

if calculation == "+":
    add()
elif calculation == "-":
    substraction()
elif calculation == "*":
    multiply()
elif calculation == "/":
    divide()