# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:12:34 2022

@author: Joseph Thomas
"""
ball_Count=20
bottle_Count=10
Book_Count=50
print("\nThe Total Numer of Items in Bag is : ",ball_Count+bottle_Count+Book_Count)
Cost_Bottle=45
print("\nTotal Cost of Bottle is : ",Cost_Bottle*bottle_Count)

#Logical Operators

a=10
b=20
print(a>b and b>10)#logical and

print(a>b or b>10) #logical or

print(not a==10)   #lgical not

#Bitwise Operators

print(a|b)         #Bitwise or

print(~b)          #Bitwise not 1's compliment of given number

print(a ^ b)       #Bitwise or 

print(b>>2)        #Bitwise rightshift

print(b<<2)        #Left Shift

#Identity Opertors

print(type(b) is int)

print(type(b) is not int)

#Membership Opertors

Names=["Joseph","Clement","James","Arun"]

print("Joseph" in Names)

print("Joseph" not in Names)


