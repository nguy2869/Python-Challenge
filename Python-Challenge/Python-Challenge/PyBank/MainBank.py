#import bank data

import os
import csv

#path to bank data

csvpath=os.path.join('..','Resources','budget_data.csv')

#csvreader

with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)

#set empty list 
    month=[]
    net=[]
    avg_change=[]
    monthly_change=[]

#loop through months 

    for row in csvreader:
        month.append(row[0])
        net.append(row[1])
    
#net total amount of "profit/losses" function 

    net_int=map(int,net)
    total_net=(sum(net_int))
    
#loop for average change in "profit/losses"

    i =0
    for i in range(len(net)-1):
        profit_loss= int(net[i+1])- int(net[i])

#append profit loss
    
        avg_change.append(profit_loss)
    Total=sum(avg_change)
    monthly_change=Total/len(avg_change)

#greatest increase function 

    profit_increase= max(avg_change)
    x=avg_change.index(profit_increase)
    month_increase =month[x+1]

#greatest decrease function 

    profit_decrease = min(avg_change)
    y=avg_change.index(profit_decrease)
    month_decrease= month[y+1]

#Print Statements 

print(f'Financial Analysis')
print(f'----------------------------')
print("Total number of months: " + str(len(month)))
print("Total net total amount over the entire period: $ " + str(total_net))
print("Average monthly change over the entire period : $" + str(monthly_change))
print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")   