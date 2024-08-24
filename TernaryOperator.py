'''a = int(input("Enter first value"))
b = int(input("Enter second value"))
c = print("a is greater than b") if a>b else print("b is greater than c")
print(c)

if c is None:
	print("c is None")
else:
	print("c is not None")'''

'''print("Program to print minimum value using ternary opertor")

a = int(input("Enter first value:"))
b = int(input("Enter second value"))
c = int(input("Enter third value"))

#	min = a if (a<b and a<c) else b if b<c else c
min = a if a<b<c else b if b<c else c
print("Minimum value:", min)'''

print("Program to print sceanrios for both number")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

value = "Both number are equal" if a==b else "a is smaller than b" if a<b else "a is greater than b"
print(value)