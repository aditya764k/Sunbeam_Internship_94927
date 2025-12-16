#Function definition

#Parameter less function
def function1():
    print("Function1")

function1()

#Parameterize Function
def function2(num1):
    print(f"Parameter is :{num1}")

function2(10)

#Function Stored in Variable

def sum(a,b):
    sum = a + b
    return sum

Addition = sum(10,20)
print(f"Addition of a & b = {Addition}")