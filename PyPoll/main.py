import os
import csv

csvpath=os.path.join('Resources','election_data.csv')

#Total de votos  #Lista de candidatos votados
#% de votos de cada candidato   # # total de votos por candidatos
#Ganador (mayor cantidad de votos)   #      BallotID,County,Candidate

ballID=[]
candidates=[]
candnames=[]             #lista de los nombres de candidatos recopilados
Totalxcand=[]            #lista de votos obtenidos x candidato

rowcount=0
TotalVotes=0
WinnerVotes=0
var1=0
var2=0
var3=0
val=0

with open(csvpath,'r') as csvfile:
    
    csvreader=csv.reader(csvfile,delimiter=',')
    csvhead=next(csvreader)

    for row in csvreader:
        TotalVotes=TotalVotes+1
        
        #print(row)
        ballID.append(row[0])
        candidates.append(row[2])
    rowcount= len(ballID)                               # total de votos en columna ballot ID

candnames.append(candidates[0])

for var1 in range (rowcount-1):
    if candidates[var1+1] != candidates[var1] and candidates[var1+1] not in candnames:
        candnames.append(candidates[var1+1])

n=len(candnames) #num de candidatos


for var2 in range(n):
    Totalxcand.append(candidates.count(candnames[var2]))



perc1=(Totalxcand[0]/TotalVotes)*100
perc2=(Totalxcand[1]/TotalVotes)*100
perc3=(Totalxcand[2]/TotalVotes)*100

for var3 in range(n):                                         #rango de var sujeto a candiatos encontrados
    Totalxcand.append(f'{Totalxcand[var3]/rowcount*100}]%')
    if Totalxcand[var3]> WinnerVotes:
        winner=candnames[var3]
        WinnerVotes=Totalxcand[var3]




print('Election Results')
print('------------------------------------')
print(f'TotalVotes: {TotalVotes}')
print('------------------------------------')
print(f'{candnames[0]}: {perc1}% ({Totalxcand[0]})')
print(f'{candnames[1]}: {perc2}% ({Totalxcand[1]})')
print(f'{candnames[2]}: {perc3}% ({Totalxcand[2]})')
print('------------------------------------')
print(f'Winner:{winner}')
print('------------------------------------')
    
    
with open('main_PyPoll.txt', 'w') as f:
    f.write(f'Election Results\n')
    f.write(f'------------------------------------------------\n')
    f.write(f'TotalVotes: {TotalVotes}\n')
    f.write(f'------------------------------------------------\n')
    f.write(f'{candnames[0]}: {perc1}% ({Totalxcand[0]})\n')
    f.write(f'{candnames[1]}: {perc2}% ({Totalxcand[1]})\n')
    f.write(f'{candnames[2]}: {perc3}% ({Totalxcand[2]})\n')
    f.write(f'------------------------------------------------\n')
    f.write(f'Winner:{winner}\n')
    f.write(f'------------------------------------------------\n')