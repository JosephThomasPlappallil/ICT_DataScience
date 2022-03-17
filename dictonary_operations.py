# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:58:59 2022

@author: Joseph Thomas
"""
#To practice dictonary operations
employee={'Name':'James',
          'Emp_Number':'E045',
          'Join_year':2021}
print(employee.get('Name'))
employee['Emp_Number']='E048'
employee['Last_Company']='strebentechnik'
print(employee)
del employee['Last_Company']
employee2=employee.copy()