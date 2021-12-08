import numpy as np
from itertools import groupby, chain
from operator import itemgetter

with  open('input.txt') as f:
	mvmnt = f.readlines()

depth = 0
horiz = 0

all_instr = np.asarray([x.split() for x in mvmnt])

for instr in all_instr:
	if instr[0][0]=='f':
		horiz+=int(instr[1])
	elif instr[0][0] == 'u':
		depth-=int(instr[1])
	else:
		depth+=int(instr[1])
print(f"depth: {depth}, horiz: {horiz}, mult: {depth*horiz}")

depth = 0
horiz = 0
aim = 0

for instr in all_instr:
	if instr[0][0]=='f':
		horiz+=int(instr[1])
		depth+=int(instr[1])*aim
	elif instr[0][0] == 'u':
		aim-=int(instr[1])
	else:
		aim+=int(instr[1])

print(f"depth: {depth}, horiz: {horiz}, mult: {depth*horiz}")

