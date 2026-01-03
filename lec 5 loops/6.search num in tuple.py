tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a number:"))
i=0
while i<len(tup):
   if (tup[i]==x):
      print("Found at idx:",i)
      break
   i+=1
else:
      print("not found")

