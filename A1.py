'''
Assignment 3
'''

#Ques1

s=input("Enter a string: ")
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(str(d))