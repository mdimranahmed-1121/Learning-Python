f=open("lec 7 file i\o\demo.txt", "r")
line1=f.readline()
line2=f.readline()
data=f.read()
print(line1)
print(line2)
print(data)

f.close()