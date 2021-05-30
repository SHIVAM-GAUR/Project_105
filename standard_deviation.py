import math
import csv

data = [60,61,65,63,98,99,90,95,91,96]

def mean(data):
    n= len(data)
    total =0
    for i in data :
        total +=  int(i)
        
    mean = total/n
    return mean

squares_list = []
for number in data :
    a = int(number) - mean(data)
    a = a**2
    squares_list.append(a)
    
sum = 0
for i in squares_list : 
    sum = sum + i
    
    
result = sum / (len(data)-1)      

std_deviation = math.sqrt(result)

print(std_deviation)  