import numpy as np
from tqdm import tqdm

#with open('test.txt') as f:
with open('input.txt') as f:
	lines = f.read().splitlines()
lines = [list(map(int,list(x))) for x in lines]

#print(lines)

def burster(board, start_count):
	temp_board = board.copy()
#	print(temp_board)
	for i, line in enumerate(board):
		for j, char in enumerate(line):
			#print([board[x] for x in nbrs])
			if char == 10:
				nbrs = [(i-1, j-1), (i-1, j), (i-1, j+1),
					(i, j-1), (i, j), (i, j+1),
					(i+1, j-1), (i+1, j), (i+1, j+1)]

				nbrs = list(set([tuple(np.abs(list(x))) for x in nbrs
					if x[0]<board.shape[0]
					and x[1]<board.shape[1]]))

				for loc in nbrs:
					if temp_board[loc]<10 :
						temp_board[loc] += 1
				temp_board[i,j]+=1
	#print(temp_board)
	count = len(np.where(temp_board>9)[0])

	#print(f'count: {count}')
	count_two = 0
	if count>start_count:
		[temp_board, count_two] =  burster(temp_board, count)
		#count+=count_two


	return([temp_board,count])

board = np.asarray(lines.copy())

sum = 0
final = 0
print(board)
i = 0
while final == 0:
	i+=1
	print(i+1)
	board = np.add(board, 1)
	[board, count] = burster(board, 0)
	count = len(np.where(board>9)[0])
	count_opp = len(np.where(board==0)[0])
	board = np.where(board>9, 0, board)
	if count == 100 or count_opp == 100:
		final = i
	print(f'FINAL: \n{board}')
	sum+=count
	if i == 100:
		sum_cent = sum

print(f'after 100 gens, {sum_cent} octopi have burst')
print(f'final step is {final}')
