# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:50:48 2022

@author: james
"""

#Assignment 5: Creating a TO DO List 
#James Sharma
#Log (Who, What, When)
#James Sharma, Developed Software, November 13


#--DATA--
#Declare Variables and Constants
strFile= "ToDoList.txt"
strData=""
dicRow={}
lstRow=[]
lstTable=[]
strMenu=""
strChoice=""

#--Processing--
#Create a text file called ToDoList.txt

objFile = open(strFile, 'r')
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"task": lstRow[0].strip(), "priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()


#Create Menu using while loop
while(True):
    print("""
    Menu of Options
    1) Show Current Data
    2) Add a New Task
    3) Remove an Existing Task
    4) Save Data to File
    5) Exit Program
    """)
    strChoice=str(input("Which option do you want to perform? [1-5]"))
    print()
    #Show Current Data Option
    if(strChoice.strip()=='1'):
      print("Your Current To DO List with Priority Level")
      for row in lstTable:
          #print(row)
          print('|-', row['task'], '-|-', row['priority'], sep='', end='\n')
          continue 
    elif(strChoice.strip()=='2'):
           print('Type in a task and level of priority for your task')
           task=input('Enter a task:')
           priority=input('Enter a priority (Low, Medium, High):')
           dicRow = {"task": task, "priority": priority} 
           lstTable.append(dicRow) 
           print(lstRow)
           continue
    elif(strChoice.strip()=='3'):
        #Remove specific item 
        if lstTable:
            remove_task = input("Which Task Would You Like To Remove?")
        for row in lstTable:
            if row['task'] == remove_task:
              lstTable.remove(row)
              print('Task Removed')
            else:
              input('The Task You Entered Does Not Exist')
        continue
    elif(strChoice.strip()=='4'):
        objFile=open(strFile, 'w')
        for row in lstTable: 
            objFile.write(str(row['task']) + ',' + str(row['priority']) + '\n')
        objFile.close()
        print('Data was saved!')
        continue
    elif(strChoice.strip()=='5'):
        print("You have chosen to exit the program")
        break  # and Exit the program
    else: 
         print('Please choose only option 1, 2, 3, 4, or 5!')
print('Done!')
 