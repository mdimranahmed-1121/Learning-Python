def recursive(n):
    if n==0:
        return 0
    sum= n+recursive(n-1)
    return sum
    
print(recursive(10))