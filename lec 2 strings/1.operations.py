#creating strings
str1="This is a string."
str2='Imran'
str3='''Ahmed'''
str4="I'm 26 years old."
str5="On the edge of a quiet fishing village, an old man named Harun lit the last lantern every night.\n No one knew why—there was electricity now, and the sea no longer needed guiding lights."
#concatenation:
print(str1)
print(str2+' '+str3+'.'+str4)
print(str5)
#length of string
print(len(str5))
#indexing
print(str5[0:80])
#slicing
print(str5[1:5])
print(str5[:5])#same as str5[0:5]
print(str5[1:])#same as str5[1:len(str5)]
#negative indexing
print(str1[-10:-1])
print(str1[::-1])