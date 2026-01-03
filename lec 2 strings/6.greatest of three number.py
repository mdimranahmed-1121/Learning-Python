num1,num2,num3=int(input()),int(input()),int(input())
if num1>=num2 and num1>=num3:
    print("Largest number:",num1)
elif num2>=num3:
    print("Largest number:",num2)
else:
    print("Largest number:",num3)