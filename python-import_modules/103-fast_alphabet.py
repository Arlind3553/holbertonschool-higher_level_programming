#!/usr/bin/python3
from itertools import accumulate, starmap, repeat
print(''.join(list(starmap(chr, zip(accumulate(repeat(1,26),initial=65))))),end='\n')
