import sys
import collections

with open('day2input.txt', 'r') as f:
    lines = f.readlines()
    count2 = count3 = 0
    for i in lines:
        a = collections.Counter(i)
        if (2 in a.values()):
            count2 += 1
        if (3 in a.values()):
            count3 += 1
    sys.stdout.write(f'{str(count2*count3)}')
