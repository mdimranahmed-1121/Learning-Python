f=open("new file.txt","a")
f.write("This is a new line.")
f.close()

f1=open("new file.txt",'r')
data=f1.read()
print(data)
f1.close()