# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:06:05 2024

@author: marcj
Problem 03
"""
class employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
        self.hierarchy={"Regular":1,"Experienced":2,"Boss":3} # defined hierarchy for later "commission" class
    def calculate_salary():
        salary=50 # base salary for an hour of work
        return salary
        
class hourly(employee):
    def calculate_salary_hr(self,hours):
        salary=employee.calculate_salary()*hours  # salary after specified time per hour
        print(f"Salary of employee {self.name} of position {self.position} after {hours}h shift>>> ${salary}")
        return salary

class setsal(employee):
    def calculate_salary_set(self,setting): # set salary directly
        print(f"Salary of employee {self.name} of position {self.position} >>> ${setting}")
        
class comms(employee):
    def calculate_salary_com(self):
        salary=employee.calculate_salary()*self.hierarchy[self.position] # salary based on hierarchy of position
        print(f"Salary of employee {self.name} of position {self.position} based on hierarchy {self.hierarchy[self.position]} >>> ${salary}")
        return salary

def main():
    l=[["Marc Jalkh","Regular","Salaried"],
       ["FN 2187","Experienced","Hourly"],
       ["Colonel Whatsapp","Boss","Commissioned"],
       ["Alien 1","Outworldly","????"]] #list of employees and their attributes
    # loop to automatically compute salary based on type of renumeration
    for i in range(len(l)):
        if "Hourly" in  l[i]:
            x=hourly(l[i][0],l[i][1]) # creates object
            x.calculate_salary_hr(30) # computes salary based on 30 hours of work
        elif "Salaried" in l[i]:
            x=setsal(l[i][0],l[i][1]) # creates object
            x.calculate_salary_set(10000) # computes salary based on given 10000 sum
        elif "Commissioned" in l[i]:
            x=comms(l[i][0],l[i][1]) # creates object
            x.calculate_salary_com() # computes salary based on position importance
        else:
            print(f"Salary computation of {l[i][1]} employee {l[i][0]} of position {l[i][2]} unavailable...")      

main()
