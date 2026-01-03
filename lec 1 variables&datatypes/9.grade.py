marks=int(input('Enter marks:'))
if marks>100 or marks<0:
    print('Invalid input.')
elif marks>=90:
    print('A+')
elif marks>=80 and marks<90:
    print('A')
elif marks>=70 and marks<80:
    print('A-')
elif marks>=60 and marks<70:
    print('B+')
elif marks>=50 and marks<60:
    print('B')
elif marks>=40 and marks<50:
    print("C")
else:
    print('Fail!')