import csv
import os
# Define Path
file = os.path.join("raw_data","budget_data_2.csv")

# Creat lists for columns of csv
date = []
revenue = []

# Read data in
with open(file) as csvfile :
    csvread = csv.reader(csvfile)

    #skips first row/header
    next(csvread, None)

    for row in csvread:
        date.append(row[0]) # add date values into Date list
        revenue.append(int(row[1])) # add revenue values into Revenue list

#The total number of months included in the dataset
datalength = len(date)

#The total amount of revenue gained over the entire period
revgrowth = revenue[-1] - revenue[0]

#The average change in revenue between months over the entire period
change_list = []
greatest_inc = -999999999999999
greatest_dec = 99999999999999999
greatest_inc_mon = ""
greatest_dec_mon = ""

for x in range(1, datalength):
    change = revenue[x] - revenue[x-1]
    change_list.append(change)
    if change > greatest_inc:
        greatest_inc = change   
        greatest_inc_mon = date[x]
    
    if change < greatest_dec:
        greatest_dec = change   
        greatest_dec_mon = date[x]
avg_change = sum(change_list) / len(change_list)  

output_dest = "pybank_result_2.csv"

# output destination in write mode and prints the summary
with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(datalength) + '\n')
    writefile.writelines('Total Revenue Gained: $' + str(revgrowth) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(avg_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + greatest_inc_mon + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + greatest_dec_mon + ' ($' + str(greatest_dec) + ')'+ '\n')

#opens the output file in r mode and prints to terminal
with open(output_dest, 'r') as readfile:
    print(readfile.read())

      