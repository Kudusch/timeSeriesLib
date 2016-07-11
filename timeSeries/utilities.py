#!/usr/bin/python

import string
import random
import re

def stampToSeconds(stamp):
    stamp = stamp.split(':')
    out = 0
    for n in stamp:
        out += int(n) * (60**list(reversed(stamp)).index(n))
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
    
def validateOptions(options):
    try:
        raw = open(options, 'r').read()
        start = re.findall(re.compile(ur'^Start: (\S*)$', re.MULTILINE) , raw)[0]
        end = re.findall(re.compile(ur'^End: (\S*)$', re.MULTILINE) , raw)[0]
        delimiter = re.findall(re.compile(ur'^Delimiter: (\S*)$', re.MULTILINE) , raw)[0]
        maxSeconds = int(re.findall(re.compile(ur'^Duration: (\S*)$', re.MULTILINE), raw)[0])
        var = re.findall(re.compile(ur'^Variable: (\S*)$', re.MULTILINE) , raw)
        values = re.findall(re.compile(ur'^Values: (\S*)$', re.MULTILINE) , raw)
        for x in [start, end, delimiter, maxSeconds, var, values]:
            if x == "" or x == [] :
                return False
        return [start, end, delimiter, maxSeconds, var, values]
    except:
        return False