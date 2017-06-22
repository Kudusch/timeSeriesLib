#!/usr/bin/python

from core import *
import datetime
import csv
import timeit

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