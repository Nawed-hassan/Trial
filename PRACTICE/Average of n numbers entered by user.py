#Average of n numbers entered by user
a=int(input("Enter the number of numbers to be averaged: "))
total=0
for i in range(a):
    c=int(input(f"Enter a number {i+1}: "))
    total += c

if a>0:
    avg=total/a
    print(f'Average of {a} numbers entered by you is: {avg}')
else:
    print('Something went wrong!')