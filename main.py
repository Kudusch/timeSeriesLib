#!/usr/bin/python

from utilities import *
import csv
import datetime
import os

def generateTimeSeries(start, end, var, values, delimiter, maxSeconds, data):
    reader = csv.reader(open(data, 'r', ), delimiter=delimiter)
    header = reader.next();

    values = values.split(',')
    timeSeries = dict((i, []) for i in range(maxSeconds+1))

    startIndex = header.index(start)
    endIndex = header.index(end)
    varIndex = header.index(var)

    for row in reader:
        if (row[varIndex] in values):
            for second in range(stampToSeconds(row[startIndex]), stampToSeconds(row[endIndex]) + 1):
                timeSeries[second].append(row[varIndex])

    now = datetime.datetime.today()
    fileName = var+"_"+now.strftime("%Y-%m-%d %H.%M.%S.csv")
    writer = csv.writer(open(fileName, 'w'), delimiter=delimiter)
    columns = csv.writer(open('columns.csv', 'w'), delimiter=delimiter) if not os.path.isfile('columns.csv') else False
    try:
        columns.writerow(["Sekunden", "Zeitstempel"])
    except:
        pass
    header = []
    header.extend([(var + ":" + x) for x in values])
    writer.writerow(header)

    for second, value in timeSeries.items():
        row = []
        row.extend(flatten(value, values))
        writer.writerow(row)
        try:
            columns.writerow([second, secondsToStamp(second)])
        except:
            pass
    
    return fileName