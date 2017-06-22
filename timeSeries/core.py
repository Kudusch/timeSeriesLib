#!/usr/bin/python

from utilities import *
import datetime
import csv
import timeit
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

def mode1(options, data):
    # read options, handle errors
    try:
        options = validateOptions(options)
        if (options == False):
            sys.exit('Error: Options are in wrong format.')   
    except:
        sys.exit('Error: Options not found.')
    try:
        if not (os.path.isfile(data)):
            sys.exit('Error: No data found.')    
    except:
        sys.exit('Error: Data not found.')

    start = options[0]
    end = options[1]
    delimiter = options[2]
    maxSeconds = options[3]
    cumulation = options[4]
    var = options[5]
    values = options[6]

    # run for every var/values pair, array with file names
    files = []
    for option in var:
        files.append(generateTimeSeries(start, end, option, values[var.index(option)], delimiter, maxSeconds, cumulation, data))
    random = id_generator()
    # after run, delete temp and columns files

    for f in files:
        currentFile = open(f, 'r')
        current = csv.reader(currentFile, delimiter=delimiter)
        # on first var/values pair merge with columns, then with temp.csv
        if files.index(f) > 0:
            writerFile = open(random+'temp.csv', 'w')
            readerFile = open(random+'merged.csv', 'r')
            writer = csv.writer(writerFile, delimiter=delimiter)
            reader = csv.reader(readerFile, delimiter=delimiter)
        else:
            writerFile = open(random+'merged.csv', 'w')
            readerFile = open('columns.csv', 'r')
            writer = csv.writer(writerFile, delimiter=delimiter)
            reader = csv.reader(readerFile, delimiter=delimiter)
        for row in current:
            next = reader.next()
            next.extend(row)
            writer.writerow(next)
        try:
            os.rename(random+'temp.csv', random+'merged.csv')
        except:
            pass
        currentFile.close()
        writerFile.close()
        readerFile.close()
        os.remove(f)
    os.remove('columns.csv')
    now = datetime.datetime.today()
    fileName = now.strftime("%Y-%m-%d %H.%M.%S.csv")
    os.rename(random+'merged.csv', fileName)

    if not cumulation == 1:
        try:
            os.rename(cumulateTo(cumulation, fileName), "cumulated_"+fileName)
            os.remove(fileName)
            os.rename("cumulated_"+fileName, fileName)
        except:
            sys.exit('Error: Cumulation failed.')
            
    return fileName 

def mode2(options, data):
    
    return fileName
    
