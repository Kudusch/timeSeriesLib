#!/usr/bin/python

import string
import random

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