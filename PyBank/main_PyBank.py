import os
import csv

csvpath = 'budget_data.csv'
month = []
profitlosses = []
difflist = []
counter = 0

def maxfinder(difflistplaceholder):
    for i in range(len(difflistplaceholder)):
        if difflistplaceholder[i] == max(difflistplaceholder):
            return i

def minfinder(difflistplaceholder1):
    for i in range(len(difflistplaceholder1)):
        if difflistplaceholder1[i] == min(difflistplaceholder1):
            return i

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    print(header)
    for row in csvreader:
        month.append(row[0])
        profitlosses.append(float(row[1]))
    print("Total Months:" + str(len(month)))
    total = (sum(profitlosses))
    print("Total: $", total)

    #-1 as you have one less integer to subtract to 
    for i in range(len(profitlosses)-1):
        difference = (profitlosses[i+1] - profitlosses[i])
        difflist.append(float(difference))
    print("Average Change: $", (sum(difflist)/len(difflist))) #how to do decimals?
    
    MaxMonth = (month[maxfinder(difflist)+1])
    MinMonth = (month[minfinder(difflist)+1])
    print("Greatest Increase in Profits:", MaxMonth, "$", max(difflist))
    print ("Greatest Decrease in Profits:", MinMonth, "$", min(difflist))


f = open("output.txt","w+")
f.write(str(total))
f.close()



    





    
        

     #if you indent you print line by line. need to exit for loop to print single line. 
    

