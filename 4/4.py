import numpy as np
from operator import methodcaller

with open('input.txt') as f:
	lines = np.asarray(f.read().splitlines())

lines = lines[lines!='']
#print(len(lines))

input = np.asarray(lines[0].split(',')).astype(int).tolist()
block1 = np.asarray(lines[2:7])
#print(block1)
#print(list(enumerate(block1)))
all_board = {}
for i,chunk in enumerate(np.arange(1,len(lines[1:]),5)):
	i+=1
#	print(lines[chunk:chunk+5])
	board = []
	for line in lines[chunk:chunk+5]:
		line = np.asarray(line.split(' '))
		line = line[line!=''].astype(int).tolist()
		board.append(line)
	board = np.asarray(board)
#	print(board.shape)
	b = board.tolist()
	t = board.T.tolist()
	b.extend(t)
#	print(b)
	all_board[i] = np.asarray(b)

called = input[:4]
done = False
for num in np.arange(4, len(input)):
	if done:
		break
	called.append(input[num])
	for board in all_board.keys():
		curr_board = all_board[board]
		for line in curr_board:
			if np.all([x in called for x in line]):
				print(curr_board[:5])
				unchecked = [x for x in curr_board[:5].ravel() if x not in called]
				print(unchecked)
				sumbrd = np.sum(unchecked)
				print(sumbrd)
				print(f"w/ {called[-1]}, board {board} won! = {called[-1]*sumbrd}")	
				done = True

called = input[:4]
done = False
board_copy = all_board.copy()
for num in np.arange(4, len(input)):
	if done:
		break
	called.append(input[num])
	for board in all_board.keys():
#		print('starter')
		if board not in board_copy.keys():
			continue
#		print(f"testing {board} w/ {called[-1]}, left = {len(board_copy.keys())}")
		curr_board = all_board[board]
		popper = False
		for line in curr_board:
			if np.all([x in called for x in line]):
				popper = True
				if len(board_copy.keys())==1:
					print(curr_board[:5])
					unchecked = [x for x in curr_board[:5].ravel() if x not in called]
					print(unchecked)
					sumbrd = np.sum(unchecked)
					print(sumbrd)
					print(f"w/ {called[-1]}, board {list(board_copy.keys())[0]} won last! = {called[-1]*sumbrd}")	
					done = True
					popper=False
		if popper:
			board_copy.pop(board)
#			print(f"kicked {board}, left {len(board_copy.keys())}")

#		if len(board_copy.keys())==1:
#			curr_board = all_board[list(board_copy.keys())[0]]


