a=int(input("Enter 1st Number : "))
b=int(input("Enter 2nd Number : "))
c=int(input("Enter 3rd Number : "))
x=a*(b+c)
print("LHS = ",x)
y=(a*b)+(a*c)
print("RHS = ",y)

if(x==y):
    print("Distributive Law")
else:
    print("not a distributive")
