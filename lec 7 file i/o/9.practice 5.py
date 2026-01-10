with open("number.txt","r") as f:
    data=f.read()
    value=data.split(',')
    count=0
    for i in range(len(value)):
        if int(value[i])%2==0:

            count+=1
            
print(count)
