import numpy as np
from tqdm import tqdm

with open('test.txt') as f:
#with open('input.txt') as f:
	lines = f.read().splitlines()

#print(lines)

for i,line in enumerate(lines):
	lines[i] = list(map(int, list(line)))
