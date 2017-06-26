#!/usr/bin/python

import string
import random
import re
import csv

def stampToSeconds(stamp):
    stamp = stamp.split(':')
    out = 0
    out += int(stamp[0])*60*60
    out += int(stamp[1])*60
    out += int(stamp[2])
    return out
    
def secondsToStamp(seconds):
    h = seconds / 3600
    m = (seconds % 3600) / 60
    s = (seconds % 3600) % 60
    return ':'.join(['%02d' % h, '%02d' % m, '%02d' % s])
    
def flatten(l, values):
    d = dict((i, 0) for i in values)
    for item in l:
        d[item] += 1
    out = []
    for key in sorted(d.iterkeys()):
         out.append(d[key])
    return out

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    
def cumulateTo(unit, data):
    with open(data, 'r') as f:
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(f.read())
        delimiter = dialect.delimiter
        f.seek(0)
        reader = csv.reader(f, delimiter=delimiter)
        header = reader.next()
        readerLength = sum(1 for row in reader)
    with open(data, 'r') as f:
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(f.read())
        delimiter = dialect.delimiter
        f.seek(0)
        reader = csv.reader(f, delimiter=delimiter)
        header = reader.next()
        unitCumulation = [0] * len(header)
        cumulated = []
        random = id_generator()
        for row in reader:
            for n in range(0,2):
                row.pop(0)
            try:
                unitCumulation = [int(x) + int(y) for x, y in zip(unitCumulation, row)]
            except:
                pass
            line = reader.line_num - 1
            if line % unit == 0:
                cumulated.append([line / unit] + unitCumulation)
                unitCumulation = [0] * len(header)
            elif line == readerLength:
                cumulated.append([(line / unit) + 1] + unitCumulation)
        with open(random+'_cumulated.csv', 'w') as write:
            writer = csv.writer(write, delimiter=delimiter)
            for n in range(0,2):
                header.pop(0)
            header = ["Cumulation Unit:"+str(unit)] + header
            writer.writerow(header)
            writer.writerows(cumulated)
        return random+'_cumulated.csv'
    
def validateOptions(options):
    try:
        with open(options, 'r') as raw:
            raw = raw.read()
            start = re.findall(re.compile(ur'^Start: (\S*)$', re.MULTILINE) , raw)[0]
            end = re.findall(re.compile(ur'^End: (\S*)$', re.MULTILINE) , raw)[0]
            delimiter = re.findall(re.compile(ur'^Delimiter: (\S*)$', re.MULTILINE) , raw)[0]
            maxSeconds = int(re.findall(re.compile(ur'^Duration: (\S*)$', re.MULTILINE), raw)[0])
            cumulation = re.findall(re.compile(ur'^Cumulate to: (\S*)$', re.MULTILINE) , raw)[0]
            if cumulation == "None":
               cumulation = 1
            else:
               cumulation = int(cumulation)
            var = re.findall(re.compile(ur'^Variable:\s(.*)$', re.MULTILINE) , raw)
            values = re.findall(re.compile(ur'^Values:\s(.*)$', re.MULTILINE) , raw)
            for x in [start, end, delimiter, maxSeconds, cumulation, var, values]:
                if x == "" or x == [] :
                    return False
            return [start, end, delimiter, maxSeconds, cumulation, var, values]
    except:
        return False
    
def validateOptions2(options):
    try:
        with open(options, 'r') as raw:
            raw = raw.read()
            delimiter = re.findall(re.compile(ur'^Delimiter: (\S*)$', re.MULTILINE) , raw)[0]
            maxSeconds = int(re.findall(re.compile(ur'^Duration: (\S*)$', re.MULTILINE), raw)[0])
            cumulation = re.findall(re.compile(ur'^Cumulate to: (\S*)$', re.MULTILINE) , raw)[0]
            if cumulation == "None":
               cumulation = 1
            else:
               cumulation = int(cumulation)
            values = re.findall(re.compile(ur'^Values:\s(.*)$', re.MULTILINE) , raw)
            try:
                values = values[0].split(',')
            except:
                return False
            for x in [delimiter, maxSeconds, cumulation, values]:
                if x == "" or x == [] :
                    return False
            return [delimiter, maxSeconds, cumulation, values]
    except:
        return False