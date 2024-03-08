

import os
import csv

#abrirarchivo
#with open(filepath,'r') as text:  ["r" de read mode]["w" de write] 
# lines=text.read()[este le las lineas del archivo]  

csvpath=os.path.join('Resources','budget_data.csv') 


#definir listas para iterar
date=[]
profitlosses=[]


TotalBudget=0
TotalMonths=0
mescount=0
val=0
loopchng=0
avchange=0
changeM=0
delta1=0
delta_1=0
delta2=0
delta_2=0

#abrir archivo
with open(csvpath,'r') as csvfile:

    csvreader=csv.reader(csvfile,delimiter=',')
    csvhead=next(csvreader)                           #header=next(csvreader) #nos saltamos el encabezado(?)
    
    for row in csvreader:  
        TotalMonths=TotalMonths+1
        
        #print(row)
        date.append(row[0])                          #metemos  a date los valores de la primera columna
        profitlosses.append(row[1])                   #metemos a profit la segunda columna
mescount=len(date)



#TotalBudget= sum(profit)
#loop profitlosses (val como indice)


for val in range (mescount):
    TotalBudget=TotalBudget+int(profitlosses[val])          #TotalBudget

#
for loopchng in range(mescount-1):
    avchange=avchange+(float(profitlosses[loopchng+1])-float(profitlosses[loopchng]))
    changeM=float(profitlosses[loopchng+1])-float(profitlosses[loopchng]) #Cambio x mes
    
    
    if changeM>delta1:                                      #mayor incremento
        delta1=changeM
        delta_1=loopchng
    else:
        delta1=delta1
        
    if changeM<delta2:                                      #mayor decrecimiento
        delta2=changeM
        delta_2=loopchng
    else:
        delta2=delta2

cambiopromedio=avchange/(mescount-1)
greatestinc=delta1
greatestdec=delta2


print('---------------------------------------')
print('Financial Analysis')
print('---------------------------------------')
print(f'Total Months:{TotalMonths}')
print(f'Total Budget: ${TotalBudget}')
print(f'Average Change:${cambiopromedio}')
print(f'Greatest Increase in Profits:{date[delta_1+1]} (${greatestinc})')
print(f'Greatest Decrease in Profits:{date[delta_2+1]} (${greatestdec})')

with open('main_PyBank.txt', 'w') as f:
    f.write(f'Financial Analysis\n')
    f.write(f'---------------------------------------\n')
    f.write(f'Total Months: {TotalMonths}\n')
    f.write(f'Total Budget: ${TotalBudget}\n')
    f.write(f'Average Change: ${cambiopromedio}\n')
    f.write(f'Greatest Increase in Profits: {date[delta_1+1]} (${greatestinc})\n')
    f.write(f'Greatest Decrease in Profits: {date[delta_2+1]} (${greatestdec})\n')



