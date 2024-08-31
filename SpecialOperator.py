# Identity Opertors, it has 2 types a) is b) is not.
a = 10
b = 10
print(id(a))
print(id(b))
print(a is b)
print("Id are equal or not =", id(a) == id(b))


# for string

c = "sumedh"
d = "sumedh"
print(c is d)


# for list 
l1 = [10, 20, 30, 40]
l2 = [10, 20, 30, 40]

print(id(l1))
print(id(l2))

print(l1 is l2)
print(l1 == l2)

#Memebership opetor
# a) in     b) in not

s = "india is great country"
print("India" in s)

li = ["heloo", "yoi ", True]
print(True in li)