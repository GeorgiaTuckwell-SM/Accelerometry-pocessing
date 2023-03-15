import pandas as pd
import numpy as np
import os, csv, time

import time
from datetime import datetime, timedelta


directory = "Input"
output_dir = "Output"


def get_drive_start_time(filepath):
    print("checking file start time:")
    print(filepath)
    with open(filepath) as f:
        # strip newline and quotes from each line
        lines = [line.strip().strip('"') for line in f.readlines()]

    for line in lines:
        if line.startswith('DataStart'):
            # get the part after the equals character
            s = line.split('=')[-1].strip('"')
            # convert string into a python datatime
            return datetime.strptime(s, '%a %b %d %H:%M:%S %Y')


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

#
# # then label the csv data accordingly
# print('Reading ActivPAL data...')
# for file in os.listdir(directory + '/ActivPAL'):
#     if file.endswith('.csv'):
#

# search input directory for csv files
csv_files = []
for file in os.listdir(directory):
    if file.endswith('.csv'):
        csv_files.append(file)

# search input directory for dat files
dat_files = []
for file in os.listdir(directory):
    if file.endswith('.dat'):
        dat_files.append(file)

for csv_file in csv_files:
    csv_data = read_activpal_csv(os.path.join(directory, csv_file))
    csv_OnlyDrive = []
    # check every dat file that matches this csv file
    for dat_file in dat_files:
        if csv_file[:3] == dat_file[:3]:
            print(csv_file + " matches " + dat_file)

            start_time = get_drive_start_time(os.path.join(directory, dat_file))

            # add labels to period of time while driving
            for line in csv_data:
                t = convert_time_activpal_csv(float(line[0]))
                if start_time < t < start_time + timedelta(minutes=20):
                    line.append('DRIVING')
                    csv_OnlyDrive.append(line)

    # create new csv file in the output directory
    output_file = os.path.join(output_dir, csv_file[:-4] + '_labelled.csv')
    print('WRITING TO', output_file)

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_OnlyDrive)
