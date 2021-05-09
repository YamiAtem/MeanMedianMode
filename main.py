import csv
import mean
import median

with open("SOCR-HeightWeight.csv", newline="") as file:
    reader = csv.reader(file)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))

n = len(new_data)
total_sum = 0

for j in new_data:
    total_sum += j

mean = mean.calculate_mean(total_sum, n)
median = median.calculate_median(n, new_data)

