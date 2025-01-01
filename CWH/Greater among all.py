a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
d=int(input("Enter a number"))

if(a==b and a==c and a==d):
    print("Given numbers are equal!")
elif(a>b and a>c and a>d):
    print(a," is greater among all!")
elif(b>a and b>c and b>d):
    print(b," is greater among all!")
elif(c>a and c>b and c>d):
    print(c," is greater among all!")
elif(d>a and d>c and d>b):
    print(d," is greater among all!")
else:
    print("Something went wrong!1")