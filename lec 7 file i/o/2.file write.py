f=open("new file.txt","w")
f.write("I want to learn python as soon as possible.")
f.close()

f1=open("new file.txt",'r')
data=f1.read()
print(data)
f1.close()