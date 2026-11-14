
'''find sum of two numbers'''
print("sum of two numbers")


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=a+b
print("Sum of two numbers", a, "+", b, "=", c)

print("--------------------------------------------------------------------------------------------------------")

'''odd or even checker'''

print("\n"*3,"odd even checker")


num=int(input("enter a number:"))
if num%2==0:
    print("The number", num, "is even")
else:
     print("The number", num, "is odd")

print("--------------------------------------------------------------------------------------------------------")


'''factorial calculation using a loop or recursion'''

print("\n"*3)

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
facto=int(input("enter a number for factorial calculation:"))
result=fact(facto)
print("the factorial of the number is:", result)
    
print("--------------------------------------------------------------------------------------------------------")


'''List reverse'''
print("\n"*3)

def reverse_string(text):
    return text[::-1]
userinput = input("Enter a string for reverse: ")
rtext = reverse_string(userinput)
print("Reversed string:", rtext)

    
print("--------------------------------------------------------------------------------------------------------")


'''fibonacci sequence'''
print("\n"*3)

def fib(m):
    x=0
    y=1
    if m<0:
        print("invalid")
    if m==1:
        print(x)
    else:
        print(x)
        print(y)
        for i in range(2,m):
            z=x+y
            x=y
            y=z
            print(z)
number=int(input("enter the number for fibonacci sequence:"))
fib(number)

print("--------------------------------------------------------------------------------------------------------")

