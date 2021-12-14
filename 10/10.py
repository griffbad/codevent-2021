import numpy as np
from tqdm import tqdm

#with open('test.txt') as f:
with open('input.txt') as f:
	lines = f.read().splitlines()

#print(lines)


def find_close_pairs(line):
	pair_starts = []
	for i in np.arange(1, len(line)):
		#print(line[i])
		if line[i-1:i+1] == '[]':
			pair_starts.append(i-1)
			#ender = i-1 + line[i-1:].rfind(']')
			#pair_starts.append((i-1,ender))
		elif line[i-1:i+1] == '{}':
			pair_starts.append(i-1)
			#ender = i-1 + line[i-1:].rfind('}')
			#pair_starts.append((i-1,ender))
		elif line[i-1:i+1] == '()':
			pair_starts.append(i-1)
			#ender = i-1 + line[i-1:].rfind(')')
			#pair_starts.append((i-1, ender))
		elif line[i-1:i+1] == '<>':
			pair_starts.append(i-1)
			#ender = i-1 + line[i-1:].rfind('>')
			#pair_starts.append((i-1,ender))
	return pair_starts

def remove_pairs(line, pairs):
	list_line = list(line)
	for pair in pairs:
		list_line[pair] = ' '
		list_line[pair+1] = ' '
	list_line = [x  for x in list_line if x != ' ']
	return ''.join(list_line)

def find_first_closed(line):
	for i in np.arange(len(line)):
		if line[i] in [']', '}', ')', '>']:
			return line[i]

def find_closer(line):
	closers = []
	for i in line[::-1]:
		if i == '{': closers.append('}')
		elif i == '[': closers.append(']')
		elif i == '<': closers.append('>')
		elif i == '(': closers.append(')')
	return closers

def calc_score(closers):
	score = 0
	for i in closers:
		score = score * 5
		if i == ')': score += 1
		elif i == ']': score += 2
		elif i == '}': score += 3
		elif i == '>': score += 4
	return score


all_err = []
all_scores = []

for i in lines:
	line = i

	pairs = find_close_pairs(line)
	#print(f'pairs: {pairs}')
	#print(f'line: {line}')
	while pairs != [] and line!=None:
		line = remove_pairs(line, pairs)
		pairs = find_close_pairs(line)
		#print(line)

	closed = find_first_closed(line)

	score = 0

	if closed == None:
		closer = find_closer(line)
		score += calc_score(closer)
		all_scores.append(score)
	all_err.append(closed)


all_err = [x for x in all_err if x != None]

sum = 0

for err in all_err:
	if err == '>': sum+=25137
	elif err == '}': sum+=1197
	elif err == ']': sum+=57
	elif err ==')':sum+=3

print(f'for the errors of {all_err}, sum is {sum}')
print(f'completing score is {np.median(all_scores)}')
