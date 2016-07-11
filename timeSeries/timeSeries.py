#!/usr/bin/python

from core import *
import datetime
import csv
import timeit

# output timer
startTime = timeit.default_timer()

# read options, handle errors
try:
    options = validateOptions(sys.argv[1])
    if (options == False):
        sys.exit('Error: Options are in wrong format.')   
except:
    sys.exit('Error: Options not found.')
try:
    data = sys.argv[2]
    if not (os.path.isfile(data)):
        sys.exit('Error: No data found.')    
except:
    sys.exit('Error: Data not found.')

start = options[0]
end = options[1]
delimiter = options[2]
maxSeconds = options[3]
var = options[4]
values = options[5]

# run for every var/values pair, array with file names
files = []
for option in var:
    files.append(generateTimeSeries(start, end, option, values[var.index(option)], delimiter, maxSeconds, data))
random = id_generator()
# after run, delete temp and columns files
for f in files:
    current = csv.reader(open(f, 'r', ), delimiter=delimiter)
    # on first var/values pair merge with columns, then with temp.csv
    if files.index(f) > 0:
        writer = csv.writer(open(random+'temp.csv', 'w'), delimiter=delimiter)
        reader = csv.reader(open(random+'merged.csv', 'r'), delimiter=delimiter)
    else:
        writer = csv.writer(open(random+'merged.csv', 'w'), delimiter=delimiter)
        reader = csv.reader(open('columns.csv', 'r'), delimiter=delimiter)
    for row in current:
        next = reader.next()
        next.extend(row)
        writer.writerow(next)
    try:
        os.rename(random+'temp.csv', random+'merged.csv')
    except:
        pass
    os.remove(f)
os.remove('columns.csv')
now = datetime.datetime.today()
fileName = now.strftime("%Y-%m-%d %H.%M.%S.csv")
os.rename(random+'merged.csv', fileName)

stopTime = timeit.default_timer()
scriptTime = stopTime - startTime
print "\nScript run in: "+str(scriptTime)+" seconds."
print "Converted file at: '"+os.path.join(os.getcwdu(), fileName)+"'\n"