#!/bin/python3

import sys


time = input().strip()
part = time[len(time)-2:len(time)]
mmss = time[3:len(time)-2]

hh = time[:2]
if part == 'AM':
    if hh == '12':
        hh = '00'
else:
    hour = int(hh)
    if hour < 12:
        hour += 12
    hh = str(hour)

print(hh + ':' + mmss)