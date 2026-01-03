light=input("Enter a color: ")
if (light.lower()=="red"):
    print('Stop')
elif(light.lower()=='yellow'):
    print('look')
elif(light.lower()=='green'):
    print('go')
else:
    print('The light is broken.')