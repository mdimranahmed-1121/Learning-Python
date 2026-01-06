def employee(name,salary=9000):
    print(name,salary,sep='\n')
employee("imran",100000)
employee("sajib")

def emp(name,salary=30000):
    return name,salary
name,salary=emp("ashik",100000)
print(name,salary,sep='\n')