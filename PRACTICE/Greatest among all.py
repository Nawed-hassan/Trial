#Greatest among all
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
if(a>b and a>c):
    print(f'Gretest among all is: {a}')
elif(b>a and b>c):
    print(f'Gretest among all is: {b}')
elif(c>a and c>b):
    print(f'Gretest among all is: {c}')
else:
    print("Something went wrong!")