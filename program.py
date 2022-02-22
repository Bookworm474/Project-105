#Import required modules
import math
import csv

#Open file and covert it to a list
with open ("data.csv",newline="") as f:
    reader = csv.reader(f)
    filedata = list(reader)
data = filedata[0]

#STEP 1 - Function to find the mean
def mean(data):
    length = len(data)
    mean_sum = 0
    for x in data:
        mean_sum += int(x)
    mean = mean_sum / length
    return mean

#STEP 2 - Square values
sq_array = []
for n in data:
    value = int(n) - mean(data)
    value = value ** 2
    sq_array.append(value)

#STEP 3 - Sum of squared values
sq_sum = 0
for n in sq_array:
    sq_sum = sq_sum + n

#STEP 4 - Divide by one less than the number of values
quotient = sq_sum / (len(data) - 1)

#STEP 5 - Find deviation by taking square root of quotient
standard_deviation = math.sqrt(quotient)
print(standard_deviation)