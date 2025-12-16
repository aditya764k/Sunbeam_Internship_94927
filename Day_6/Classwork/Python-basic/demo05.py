#Maximum Number

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

max = 0;

if num1 > num2:
    max = num1
    print("num1 is max")
elif num1 == num2:
    print("Both are equal")
else:
    print("num2 is max")
    max = num2
    
print(f"Maximum Number is : {max}")