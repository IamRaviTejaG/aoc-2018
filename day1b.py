import sys
import time

with open('day1input.txt', 'r') as f:
    lines = list(map(int, f.readlines()))
    freq = 0
    a = []
    for _ in lines:
        freq += _
        a.append(freq)
        if (freq == 73364):
            print('YES')
