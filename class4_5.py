import os
import csv
from pylab import *

# constant variables:
NMI = 1852.0
pi = 3.14159
D2R = pi / 180


def read_csv_file(filename):
    data = []
    file = open(filename)
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


def process_gps_data(data):
    latitude = []
    longitude = []
    velocity = []
    t_seconds = []
    num_stats = []
    for row in data:
        if row[0] == '$GPGSV':
            num_stats.append(float(row[3]))
        elif row[0] == '$GPRMC':
            t_seconds.append(float(row[1][0:2]) * 3600 + float(row[1][2:4]) * 60 + float(row[1][4:6]))
            latitude.append(float(row[3][0:2]) + float(row[3][2:]) / 60)
            longitude.append(float(row[5][0:3]) + float(row[5][3:]) / 60)
            velocity.append(float(row[7]) * NMI / 10000.0)
    return (list(latitude), list(longitude), list(velocity), list(t_seconds), list(num_stats))


# Main:


for root,dirs,files in os.walk('../data'):
    for filename in files:
        # create full (absolute) path for each file
        cur_file = os.path.join(root, filename)
        if(filename.endswith('csv')):
            file_contents = read_csv_file(cur_file)
            gps_commands = list_gps_commands(file_contents)
            print("Command Frequency")
            print("....... .........")
            for command in gps_commands:
                print(command, ' ', gps_commands[command])
            (lat, long, v, t, stats) = process_gps_data(file_contents)
            figure()
            gca().axes.invert_xaxis()
            plot(long, lat, 'b', label='Cruising', linewidth=3)
            title(filename[:-4])
            legend(loc = 'upper left')
            xlabel = ('East-Wast (meters)')
            ylabel = ('South-North (meters')
            grid()
            axis('equal')
            show()

