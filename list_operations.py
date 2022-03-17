# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:30:06 2022

@author: Joseph Thomas
"""
teacher_list=["James","Clement","Alex","Arjun"]
print(teacher_list[0])
print(teacher_list[-1])
print(teacher_list[0:3])
print(teacher_list)
teacher_list[3]="David"
print(teacher_list)
teacher_list.append("Geetha")
print(teacher_list)
teacher_list.insert(2,"Ajith")
teacher_list.remove("Geetha")
teacher_list.pop(-3)
teacher_list.sort()
List2=["Blessil","Dona"]
teacher_list.extend(List2)