#!/usr/bin/python

from utilities import *
import csv
import datetime
import os
import sys

# generates csv and returns file names
def generateTimeSeries(start, end, var, values, delimiter, maxSeconds, cumulation, data):
    f = open(data, 'r', )
    try:
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(f.read())
        if not (dialect.delimiter == delimiter):
            sys.exit('Error: Data file uses different delimiter than the one set in options.')
        f.seek(0)
        reader = csv.reader(f, delimiter=delimiter)
        header = reader.next();

        values = values.split(',')
        timeSeries = dict((i, []) for i in range(maxSeconds+1))

        startIndex = header.index(start)
        endIndex = header.index(end)
        varIndex = header.index(var)

        for row in reader:
            if (row[varIndex] in values):
                for second in range(stampToSeconds(row[startIndex]), stampToSeconds(row[endIndex]) + 1):
                    try:
                        timeSeries[second].append(row[varIndex])
                    except:
                        pass

        now = datetime.datetime.today()
        fileName = var+"_"+now.strftime("%Y-%m-%d %H.%M.%S.csv")
        writerFile = open(fileName, 'w')
        writer = csv.writer(writerFile, delimiter=delimiter)
        if not os.path.isfile('columns.csv'):
            columnsFile = open('columns.csv', 'w')
            columns = csv.writer(columnsFile, delimiter=delimiter)
        else:
            False
        try:
            columns.writerow(["Second", "Timestamp"])
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
        writerFile.close()
        try:
            columnsFile.close()
        except:
            pass
        return fileName
    finally:
        f.close()