#!/c/Users/egood/AppData/Local/Programs/Python/Python35/python

import sys
from itertools import groupby


def read_distinct_input(file):
    prev_line = None
    for line in file:
        line = line.strip()
        if prev_line != line:
            prev_line = line
            yield line.split(' ', 1)


def reduce():
    for k, g in groupby(read_distinct_input(sys.stdin), lambda x: x[0]):
        print('{0} {1}'.format(k, ','.join([e[1] for e in g])))

def main():
    reduce()

if __name__ == '__main__':
    main()