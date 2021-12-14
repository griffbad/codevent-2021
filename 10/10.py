import numpy as np
from tqdm import tqdm

with open('test.txt') as f:
#with open('input.txt') as f:
	lines = f.read().splitlines()

print(lines)


def find_close_pairs(line):
	pair_starts = []
	for i in np.arange(1, len(line)):
		if line[i-1] == '[':
			ender = i-1 + line[i-1:].rfind(']') 
			pair_starts.append((i-1,ender))
		elif line[i-1] == '{':
			ender = i-1 + line[i-1:].rfind('}') 
			pair_starts.append((i-1,ender))
		elif line[i-1] == '(':
			ender = i-1 + line[i-1:].rfind(')') 
			pair_starts.append((i-1, ender))
		elif line[i-1] == '<':
			ender = i-1 + line[i-1:].rfind('>') 
			pair_starts.append((i-1,ender))
	return pair_starts

def remove_pairs(line, pairs):
	list_line = list(line)
	for pair in pairs:
		del list_line[pair[0]]
		del list_line[pair[1]]

	return ''.join(line)

def find_first_closed(line):
	for i in np.arange(len(line)):
		if line[i] in [']', '}', ')', '>']:
			return line[i] 

for i in lines:
	line = i
	
	pairs = find_close_pairs(line)
	print(f'pairs: {pairs}')
	print(f'line: {line}')
	while pairs != [] and line!=None:
		line = remove_pairs(line, pairs)
		pairs = find_close_pairs(line)
		print(line)
	
	print(find_first_closed(line))
