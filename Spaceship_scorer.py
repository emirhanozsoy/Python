# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:20:39 2019

@author: emirhan
"""

number_of_spaceships=-1
while number_of_spaceships<=0 or number_of_spaceships>=70001:
        print('Please enter spaceship number(Must be between 0-70000):')
        number_of_spaceships=int(input())
        
spaceshipID=0
spaceshipIDs=[]
spaceshipTimes=[]
counter=0
matrix=[]
scores =[]


for i in range(number_of_spaceships):
    row=[]
    for j in range(3): 
        row.append(0) 
    matrix.append(row) 
    
for i in range(number_of_spaceships):
    row=[]
    for j in range(2): 
        row.append(0) 
    scores.append(row) 


while counter <= number_of_spaceships:
    if counter==number_of_spaceships:
        break
    print('Please enter spaceshipID',counter,' StartTime and EndTime:')
    a, b, c = map(int, input().strip().split())
    if a in spaceshipIDs:
        print('Id Must be Unique')
    else:
        if b in spaceshipTimes:
            print('Time Must be Unique')
        else:
            if c in spaceshipTimes:
                print('Time Must be Unique')
            else:
                if int(b) > int(c):
                    print('Start Time must be smaller then End Time',spaceshipID.split()[1],'>',spaceshipID.split()[2])
                else:
                    matrix[counter][0]=int(a)
                    matrix[counter][1]=int(b)
                    matrix[counter][2]=int(c)
                    spaceshipIDs.append(int(a))
                    spaceshipTimes.append(int(b))
                    spaceshipTimes.append(int(c))
                    scores[counter][0]=int(a)
                    counter=counter+1
    
for i in range(0,number_of_spaceships):
    for j in range(0,number_of_spaceships):
        if matrix[i][1] < matrix[j][1]:
                if matrix[i][2] > matrix[j][2]:
                    scores[i][1]=scores[i][1]+1
             
tmp0=0
tmp1=0        
for i in range(0,number_of_spaceships):
    for j in range(0,number_of_spaceships):
        if scores[i][1]<scores[j][1]:
            tmp0,tmp1=scores[i][0],scores[i][1]
            scores[i][0],scores[i][1]=scores[j][0],scores[j][1]
            scores[j][0],scores[j][1]=tmp0,tmp1
        if scores[i][1]==scores[j][1]:
            if scores[i][0]<scores[j][0]:
                tmp0,tmp1=scores[i][0],scores[i][1]
                scores[i][0],scores[i][1]=scores[j][0],scores[j][1]
                scores[j][0],scores[j][1]=tmp0,tmp1     

for row in scores:
    print(row[0],row[1])