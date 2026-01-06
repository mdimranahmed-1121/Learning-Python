def outer(a,b):
    def inner(a,b):
        sum=a+b
        return sum
    result=inner(a,b)
    return result+5
print(outer(10,5))