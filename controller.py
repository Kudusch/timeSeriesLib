#!/usr/bin/python

from main import *
import sys
import re
import datetime
import csv
import os

options = open(sys.argv[1], 'r').read()
data = sys.argv[2]
start = re.findall(re.compile(ur'^Start: (.*)$', re.MULTILINE) , options)[0]
end = re.findall(re.compile(ur'^Ende: (.*)$', re.MULTILINE) , options)[0]
delimiter = re.findall(re.compile(ur'^Trennungszeichen: (.*)$', re.MULTILINE) , options)[0]
maxSeconds = int(re.findall(re.compile(ur'^Dauer: (.*)$', re.MULTILINE), options)[0])

var = re.findall(re.compile(ur'^Variable: (.*)$', re.MULTILINE) , options)
values = re.findall(re.compile(ur'^Werte: (.*)$', re.MULTILINE) , options)

files = []
for option in var:
	files.append(generateTimeSeries(start, end, option, values[var.index(option)], delimiter, maxSeconds, data))

for f in files:
	current = csv.reader(open(f, 'r', ), delimiter=delimiter)
	if files.index(f) > 0:
		writer = csv.writer(open('temp.csv', 'w'), delimiter=delimiter)
		reader = csv.reader(open('merged.csv', 'r'), delimiter=delimiter)
	else:
		writer = csv.writer(open('merged.csv', 'w'), delimiter=delimiter)
		reader = csv.reader(open('columns.csv', 'r'), delimiter=delimiter)
	for row in current:
		next = reader.next()
		next.extend(row)
		writer.writerow(next)
	try:
		os.rename('temp.csv', 'merged.csv')
	except:
		pass
	os.remove(f)
os.remove('columns.csv')
now = datetime.datetime.today()
fileName = now.strftime("%Y-%m-%d %H.%M.%S.csv")
os.rename('merged.csv', fileName)