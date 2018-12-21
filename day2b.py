import sys
import collections


def linediff(listoflines):
    d = ''
    for _1 in range(0, len(listoflines)-1):
            for _2 in range(_1+1, len(listoflines)):
                if (len(listoflines[_1]) != len(listoflines[_2])):
                    return d
                else:
                    diff = 0
                    a = listoflines[_1]
                    b = listoflines[_2]
                    c = len(a)
                    for _ in range(c):
                        if (a[_] != b[_]):
                            diff += 1
                    if (diff == 1):
                        for _ in range(c):
                            if (a[_] != b[_]):
                                d = a[:_] + a[_+1:]
    return d


with open('day2input.txt', 'r') as f:
    lines = f.readlines()
    a = linediff(lines)
    sys.stdout.write(f'{a}')
