#Average of n numbers
#Fact() is a function to find factorial
def fact(k):
    if (k==0 or k==1):
        return 1 #if the value of k =0 or 1 it will return 1 as value
    else:
        return k + fact(k-1)

n=int(input("Enter a number of number(s) of which average is to be find: "))

for i in range (n):
    c=fact(n)/n
print(c)