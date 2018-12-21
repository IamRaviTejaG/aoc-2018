import sys

with open('day1input.txt', 'r') as f:
    lines = map(int, f.readlines())
    sys.stdout.write(f'{str(sum(list(lines)))}')
