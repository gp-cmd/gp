a=int(input("Enter 1st Number : "))
b=int(input("Enter 2nd Number : "))
c=int(input("Enter 3rd Number : "))
x=a+(b+c)
print("LHS = ",x)
y=(a+b)+c
print("RHS = ",y)
if(x==y):
    print("Associative Law")
else:
    print("not  Associative Law")
print("\n")
p=a*(b*c)
print("LHS = ",p)
q=(a*b)*c
print("LHS = ",q)
if(p==q):
    print("Associative law")
else:
    print("not  Associative law")
