tup = (1,4,9,16,25,36,49,64,81,90,100)
n = int(input())

for i in tup:
    if i == n:
        print("found at:")
        break
else:
    print("not in this tuple.")

li = [1,4,9,16,25,36,49,64,81,90,100]
for i in li:
    print(i)
