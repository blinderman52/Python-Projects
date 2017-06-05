import os
import csv
from pylab import *


def read_csv_file(file_name):
    data = []
    file = open(file_name)
    csvfile = csv.reader(file)
    for row in csvfile:
        # print(row)
        data.append(row)
    file.close()
    return data


def list_gps_commands(data):
    gps_cmds = dict()
    for row in data:
        try:
            gps_cmds[row[0]] += 1
        except KeyError:
            gps_cmds[row[0]] = 1
    return gps_cmds




# === Main ====
# filename = 'GPS-2008-05-30-09-00-50.csv'
filename = 'GPS-2008-06-04-09-03-45.csv'

file_contents = read_csv_file(filename)

print(filename)
print('The number of records in the file is: ', len(filename))

# Create a dictionary of GPS commands and their frequencies
gps_commands = list_gps_commands(file_contents)
x_data = []
x_label = []

for command in gps_commands:
    print(command, ' ', gps_commands[command])
    x_data.append(gps_commands[command])
    x_label.append(command)


figure()
# y = [1, 2, -1, 1]
# x = [10, 11, 12, 13]
# plot(x, y, 'D-.')
# title('Simple Plots')
# i = arange(6)
# plot(i, sin(i), 'k+-', i, cos(i), 'm:')
# plot(i, sin(i), lw=8)
# plot(i, cos(i), lw=2)
# title('plot')
# show()

bars = arange(len(x_data))
bar(bars, x_data, align='center')
xticks(bars, x_label, rotation='-10')
ylabel("Number of Unique Commands")
title('Unique GPS Commands')
show()
