# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:03:13 2022

@author: Joseph Thomas
"""
number=int(input("Enter the number : "))
if number%2==0:
    print("\n  ",number,"is Even")
else:
    print("\n  ",number,"is Odd")
    
#if elif

if number>0:
    print("\n  ",number,"is positive")
elif number<0:
    print("\n  ",number,"is -ve")
else:
    print("\n  ",number,"is neither +ve nor -ve")
    
    
#loop Statements
#for loop
sum=0
mark=[20,80,70,55,60,32]

for i in mark:
    sum+=i

print(sum)

#While loop

sum1=0
i=0
while(i<=number):
    sum1+=i
    i=i+1
print("Sum = ",sum1)

#Break and continue

#break
Employee="Arjun"

for i in Employee:
    if(i=='j'):
        break
    print(i)
    
#Continue

for i in Employee:
    if(i=='j'):
        continue
    print(i)
