
def fact(n):
    f=1
    if n==0:
        print("factorial does not exist.")
    elif n>=1:
        for i in range(1,n+1):
            f= f*i
    return f        
print(fact(int(input("Enter a value:"))))