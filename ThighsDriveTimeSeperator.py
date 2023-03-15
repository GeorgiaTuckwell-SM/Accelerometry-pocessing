import pandas as pd
import numpy as np
import os, csv, time

import time
from datetime import datetime, timedelta

#Make sure all .dat files were in chronological order before beginning this code-it will not work or you will lose some drive files.
directory = "Input"
output_dir = "Output"

def read_activpal_csv(filepath):
    with open(filepath) as f:
        # strip newline from each line
        lines = [line.strip() for line in f.readlines()]

    # determine the seperator character for this file
    if lines[0].startswith('sep'):
        sep = lines[0].split('=')[-1].strip()
        lines = lines[1:]
    else:
        sep = ','

    # column names are on the first line
    column_names = lines[0]
    lines = lines[1:]

    # break up each each line using the seperator
    for n, line in enumerate(lines):
        lines[n] = line.split(sep)

    return lines

def convert_time_activpal_csv(input_time):

    # times in excel are recorded as number of days since this day:
    t0 = datetime(1899, 12, 30)

    # so we add input_time days to the above date
    return t0 + timedelta(days=input_time)

# search input directory for csv files
csv_files = []
for file in os.listdir(directory):
    if file.endswith('.csv'):
        csv_files.append(file)

for csv_file in csv_files:
    csv_data = read_activpal_csv(os.path.join(directory, csv_file))

    Day1Morning, Day1Afternoon, Day2Morning, Day2Afternoon, Day3Morning, Day3Afternoon, Day4Morning, Day4Afternoon, Day5Morning, Day5Afternoon = [],[],[],[],[],[],[],[],[],[]
    day = 1
    Previous = convert_time_activpal_csv(float(csv_data[0][0]))
    for line in csv_data:
        t = convert_time_activpal_csv(float(line[0]))

        if t.day != Previous.day:
            day +=1

        #CASE
        if day == 1:
            if t.hour < 13:
                Day1Morning.append(line)
            else:
                Day1Afternoon.append(line)
        elif day == 2:
            if t.hour < 13:
                Day2Morning.append(line)
            else:
                Day2Afternoon.append(line)
        elif day == 3:
            if t.hour < 13:
                Day3Morning.append(line)
            else:
                Day3Afternoon.append(line)
        elif day == 4:
            if t.hour < 13:
                Day4Morning.append(line)
            else:
                Day4Afternoon.append(line)
        elif day == 5:
            if t.hour < 13:
                Day5Morning.append(line)
            else:
                Day5Afternoon.append(line)

        Previous = t

    # create new csv file in the output directory
    Day1MorningFile = os.path.join(output_dir, csv_file[:-4] + '_D1_M.csv')
    Day1AfternoonFile = os.path.join(output_dir, csv_file[:-4] + '_D1_A.csv')
    Day2MorningFile = os.path.join(output_dir, csv_file[:-4] + '_D2_M.csv')
    Day2AfternoonFile = os.path.join(output_dir, csv_file[:-4] + '_D2_A.csv')
    Day3MorningFile = os.path.join(output_dir, csv_file[:-4] + '_D3_M.csv')
    Day3AfternoonFile = os.path.join(output_dir, csv_file[:-4] + '_D3_A.csv')
    Day4MorningFile = os.path.join(output_dir, csv_file[:-4] + '_D4_M.csv')
    Day4AfternoonFile = os.path.join(output_dir, csv_file[:-4] + '_D4_A.csv')
    Day5MorningFile = os.path.join(output_dir, csv_file[:-4] + '_D5_M.csv')
    Day5AfternoonFile = os.path.join(output_dir, csv_file[:-4] + '_D5_A.csv')

    print('WRITING TO', Day1MorningFile)

    with open(Day1MorningFile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(Day1Morning)

    print('WRITING TO', Day1AfternoonFile)

    with open(Day1AfternoonFile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(Day1Afternoon)

    print('WRITING TO', Day2MorningFile)

    with open(Day2MorningFile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(Day2Morning)

    print('WRITING TO', Day2AfternoonFile)

    with open(Day2AfternoonFile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(Day2Afternoon)

    print('WRITING TO', Day3MorningFile)

    with open(Day3MorningFile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(Day3Morning)

    print('WRITING TO', Day3AfternoonFile)

    with open(Day3AfternoonFile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(Day3Afternoon)

    print('WRITING TO', Day4MorningFile)

    with open(Day4MorningFile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(Day4Morning)

    print('WRITING TO', Day4AfternoonFile)

    with open(Day4AfternoonFile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(Day4Afternoon)

    print('WRITING TO', Day5MorningFile)

    with open(Day5MorningFile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(Day5Morning)

    print('WRITING TO', Day5AfternoonFile)

    with open(Day5AfternoonFile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(Day5Afternoon)









    # PreviousTime = convert_time_activpal_csv(float(csv_data[0][0]))
    # CSV_lines_Morning = []
    # CSV_lines_Afternoon = []
    # switch = True
    # for line in csv_data:
    #     currentTime = convert_time_activpal_csv(float(line[0]))
    #     difference = currentTime - PreviousTime
    #     if divmod(difference.total_seconds(), 3600)[0] > 4:
    #         switch = False
    #     PreviousTime = currentTime
    #     if switch:
    #         CSV_lines_Morning.append(line)
    #     else:
    #         CSV_lines_Afternoon.append(line)
    #
    # # create new csv file in the output directory
    # output_file = os.path.join(output_dir, csv_file[:-4] + '_labelled.csv')
    # print('WRITING TO', output_file)
    #
    # with open(output_file, 'w', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerows(csv_OnlyDrive)
