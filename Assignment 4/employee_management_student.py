#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:49:18 2020

@author: xg7
"""

from employee_class_student import *
import pickle as pk


def main(quit_system):
    MENU = ("1.Look up\n"
            "2.Add new employee\n"
            "3.Change employee information\n"
            "4.Delete employee\n"
            "5.Quit\n"
            "Please select an operation: ") 
        

    option = input(MENU)
    
    if option not in "12345":
#        raise Exception("Invalid option!", option) 
        print("Invalid option!", option)
        return quit_system
    try:
        dbfile = open('emp_database.dat', 'rb')
        emp_dict = pk.load(dbfile)
        dbfile.close()

    except (FileNotFoundError, EOFError):
        emp_dict = {}
     
    if option == '1':
        lookUp = input("Please given the ID: ")
        try:
            theEmployee = emp_dict[lookUp]
            print("ID: {ID}\n{name}\n{dept}\n{jobtitle}".format(ID = theEmployee.get_ID(),\
              name = theEmployee.get_name(), dept = theEmployee.get_department(),\
              jobtitle = theEmployee.get_jobTitle())) 
        except KeyError:
            print("No such an ID.")
    elif option == '2':
        empInfo = input("Please given name/ID/department/job title: ")
        empInfo = empInfo.split('/')
#        print("empInfo", empInfo)
        try:
            k_id = empInfo[1]
            emp_dict[k_id] = Employee()
            emp_dict[k_id].set_name(empInfo[0])
            emp_dict[k_id].set_ID(empInfo[1])
            emp_dict[k_id].set_department(empInfo[2])
            emp_dict[k_id].set_jobTitle(empInfo[3])
        except IndexError:
            print("Incorrect input format.")
        
    elif option == '3':
        num = input('which employee information do you want to change? ID: ')
        try:
            empik = emp_dict[num]            
            changes = ["Name", "Department", "Job Title"]
            set_target = [empik.set_name, empik.set_department, empik.set_jobTitle]
            get_seed = [empik.get_name(), empik.get_department(), empik.get_jobTitle()]
            print(f"current values for employee ID {empik.get_ID()} :")
            [print(f'{n+1}) {v}: {get_seed[n]}') for n,v in enumerate(changes)]
            index = int(input("I want to change entry number:")) - 1 
            change = input(f'I would you like to change the {changes[index]} currently \"{get_seed[index]}\" to:')
            set_target[index](change)
            print("The change was successful!")
        except KeyError:
            print('there is nobody working here with such ID!!')
        except (IndexError, ValueError):
            print("ERROR")
            
            
    
    elif option == '4':
        employInfo = input("which employee do you want to delete? ID: ")
        try:
            del emp_dict[employInfo]
        except:
            print('not existing employee')
        
    elif option == '5':
        quit_system = True
        return quit_system
    
    ##saving emp_dict 
    Database = open('emp_database.dat', 'wb')
    ##your code for saving emp_dict insert goes here
    pk.dump(emp_dict, Database)                     
    
    
    Database.close()
    return quit_system

     
if __name__ == '__main__':
    
    quit_system = False
    while not quit_system:
        quit_system = main(quit_system)

