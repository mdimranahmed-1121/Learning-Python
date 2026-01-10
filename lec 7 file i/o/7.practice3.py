with open("practice.txt",'r') as f:
    data=f.read()
    if data.find('learning')!=0:
        print("Found")
    else:
        print("Not found.")